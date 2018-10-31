import os
import argparse
import requests
from BeautifulSoup import BeautifulSoup as Soup
from soupselect import select
from gooey import Gooey

FINISHERPIX_URL = "http://www.finisherpix.com/gallery/photos/en/EUR/%s/%s"

def get_photos(race, bibs, path_prefix=''):
    for bib in bibs:
        bib = bib.strip()
        bib_url = FINISHERPIX_URL % (race, bib)
        photo_list_html = requests.get(bib_url)
        soup = Soup(photo_list_html.text)
        photo_list = select(
            soup,
            '.photocommercePhotosList .photocommercePhotoFrame img.lazy')
        for photo in photo_list:
            photo_url = photo['data-original']
            photo_filename = photo_url.split('/')[-1]
            bib_dir_path = os.path.join(path_prefix, race, bib)
            if path_prefix and not os.path.exists(path_prefix):
                os.makedirs(path_prefix)
            if not os.path.exists(os.path.join(path_prefix, race)):
                os.makedirs(os.path.join(path_prefix, race))
            if not os.path.exists(bib_dir_path):
                os.makedirs(bib_dir_path)
            r = requests.get('http:%s' % photo_url, stream=True)
            if r.status_code == 200:
                with open(os.path.join(bib_dir_path, photo_filename), 'wb') \
                        as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                    print('Downloaded http:%s to %s' % (photo_url,
                                                        os.path.join(
                                                            bib_dir_path,
                                                            photo_filename)))
        return bib_dir_path
@Gooey
def main():
    parser = argparse.ArgumentParser(
        description='Simple app to download all low res images from '
                    'finisherpix.com for a given race and bib number')
    parser.add_argument('--race', action="store", dest="race",
                        required=True,
                        default="2506",
                        help="finisherpix.com tag for race. eg. "
                             "2506 for "
                             "Dublin City Marathon 2018 ")
    parser.add_argument('--bib', action="store", dest="bibs_str",
                        required=True,
                        help="Separate multiple bibs with comma")
    args = parser.parse_args()

    if not args.race:
        print("You must specify a race.")
    if not args.bibs_str:
        print("You must specify at least one bib.")

    bibs = args.bibs_str.split(",")

    get_photos(args.race, bibs)


if __name__ == '__main__':
    main()
