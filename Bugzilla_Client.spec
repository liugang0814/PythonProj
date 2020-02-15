# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main_opr.py'],
             pathex=['E:\\PythonWork\\Bugzilla'],
             binaries=[],
             datas=[(".\icon\*.ico","icon"),
                    # (".\result","result"),
                    (".\config\*","config")],
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
          name='Bugzilla_Client',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Bugzilla_Client')
