# -*- mode: python -*-

block_cipher = None


a = Analysis(['render.py'],
             pathex=['C:\\Users\\HP\\Desktop\\attendance system'],
             binaries=[],
             datas=[('C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python37-32\\lib\\site-packages\\eel\\eel.js', 'eel'), ('gui', 'gui'), ('./config.json', './')],
             hiddenimports=['bottle_websocket'],
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
          [],
          exclude_binaries=True,
          name='Meet Attendance',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='main.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Meet Attendance')
