# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['menu.py'],
    pathex=[],
    binaries=[],
    datas=[(
        r"C:\Users\User\Documents\structural_engineering\2025\ADIPSA\column_table_etabs\venv\Lib\site-packages\comtypes\gen\_F896D55D_8BDF_4232_B9AB_4B210897A81D_0_1_0.py",
        "comtypes/gen"
    )],
    hiddenimports=['comtypes', 'comtypes.client', 'comtypes.gen', 'comtypes.gen.ETABSv1'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='cuadroColApp_etabsv1',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
