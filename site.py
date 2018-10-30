#!/usr/local/bin/python2.7
import os
import zipfile
import cherrypy

from jinja2 import Environment, FileSystemLoader
from cherrypy.lib.static import serve_file

from finisherpixdownloader import get_photos


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       file.replace('web/downloads', ''))


class FinisherPixDownloader(object):
    @cherrypy.expose
    def index(self, race=None, bib=None):
        zip_path = None
        if bib and race:
            zip_path = os.path.join('web/downloads', race, '%s.zip' % bib)
            # check to see if the photos already exist
            if not os.path.exists(zip_path):
                bib_dir_path = get_photos(race, [bib],
                                          path_prefix='web/downloads')

                zipf = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
                zipdir(bib_dir_path, zipf)
                zipf.close()
        env = Environment(loader=FileSystemLoader('web/templates'))
        tmpl = env.get_template('index.html')
        return tmpl.render(zip_path=zip_path, bib=bib, race=race)

    @cherrypy.expose
    def download(self, filepath):
        return serve_file(os.path.abspath(os.path.join('.',filepath)),
                          "application/zip", "attachment")


cherrypy.config.update({
    'environment': 'production',
    'log.screen': False,
    'server.socket_host': '127.0.0.1',
    'server.socket_port': 28330,
})
cherrypy.quickstart(FinisherPixDownloader())
