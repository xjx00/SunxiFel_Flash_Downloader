# -*- mode: python -*-

block_cipher = None


a = Analysis(['gui.py'],
             pathex=['E:\\licheepi\\��֦Nano\\bpi-fel-mass-storage-gui4win-v1.002\\pack\\win32'],
             binaries=[],
             datas=[('sunxi-fel.exe','.'),('libusb-1.0.dll','.'),('libwinpthread-1.dll','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
