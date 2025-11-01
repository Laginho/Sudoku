# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\app.py'],
    pathex=[],
    binaries=[],
    datas=[('src/sudoku.kv', 'src'), ('data/sudoku_puzzles.db', 'data'), ('data/puzzles.txt', 'data'), ('assets', 'assets')],
    hiddenimports=[],
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
    name='Sudoku',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\game.ico'],
)
