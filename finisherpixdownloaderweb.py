import web
import os
import zipfile
from finisherpixdownloader import get_photos
import itertools

urls = (
    '/', 'index',
    '/downloads/(.*)', 'downloads'
)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), file.replace('web/downloads',''))


class index:

    def GET(self,):
        i = web.input(race=None, bib=None)
        zip_path = None
        if i.bib and i.race:
            bib_dir_path = get_photos(i.race, [i.bib],
                                      path_prefix='web/downloads')
            zip_path = os.path.join('web/downloads', i.race, '%s.zip' % i.bib)
            zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
            zipdir(bib_dir_path, zipf)
            zipf.close()
        render = web.template.render('web/templates/')
        return render.index(zip_path)


class downloads:
    def GET(self,name):
        web.header("Content-Type", "application/zip") # Set the Header
        return open(name,"rb").read() # Notice 'rb' for reading images



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
