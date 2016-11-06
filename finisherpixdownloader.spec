# -*- mode: python -*-

block_cipher = None


a = Analysis(['finisherpixdownloader.py'],
             pathex=['/home/philroche/PycharmProjects/finisherpixdownloader'],
             binaries=None,
             datas=[('/home/philroche/.virtualenvs/finisherpixdownloader/lib/python2.7/site-packages/gooey/images','gooey/images'),
                    ('/home/philroche/.virtualenvs/finisherpixdownloader/lib/python2.7/site-packages/gooey/languages','gooey/languages')],
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
          console=True )
