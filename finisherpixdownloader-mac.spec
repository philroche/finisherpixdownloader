# -*- mode: python -*-

block_cipher = None


a = Analysis(['finisherpixdownloader.py'],
             pathex=['/Volumes/data/Working/finisherpixdownloader'],
             binaries=None,
             datas=[('/Users/philroche/.virtualenvs/finisherpixdownloader/lib/python2.7/site-packages/gooey/images','gooey/images'),
                    ('/Users/philroche/.virtualenvs/finisherpixdownloader/lib/python2.7/site-packages/gooey/languages','gooey/languages')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='finisherpixdownloader',
          debug=False,
          strip=False,
          upx=True,
          console=False )
app = BUNDLE(exe,
             name='finisherpixdownloader.app',
             icon=None,
             bundle_identifier=None)
