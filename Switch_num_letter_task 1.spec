# -*- mode: python ; coding: utf-8 -*-

# import site
# site_pakage_position = site.getsitepackages()[-1]

block_cipher = None


a = Analysis(['Switch_num_letter_task.py'],
             pathex=['C:\\Users\\Jayce\\py_edu'],
             binaries=[
                ('C:\\python37\\Lib\\site-packages\\pyglet_ffmpeg\\Win64\\', '.'),
                ('C:\\python37\\Lib\\site-packages\\psychopy\\', '.\\psychopy\\'),
             ],
             datas=[
                 ('C:\\python37\\lib\\site-packages\\arabic_reshaper\\default-config.ini', '.\\arabic_reshaper\\'),
                 ('C:\\python37\\lib\\site-packages\\arabic_reshaper\\__version__.py', '.\\arabic_reshaper\\'),
             ],
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
          [],
          exclude_binaries=True,
          name='Switch_num_letter_task',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Switch_num_letter_task')
