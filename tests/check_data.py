"""Regenerate every dataset with code/data/make_data.py on every Python
version you have, and check that the files are identical to the ones in code/data.

Usage: python tests/check_data.py
"""
import filecmp
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "code" / "data"
# The Python running this script, or every .venvs/py3.x if you made them.
_VENVS = {v: ROOT / ".venvs" / f"py{v}" / "bin" / "python"
          for v in ("3.15", "3.14", "3.13", "3.12")}
PYTHONS = {v: p for v, p in _VENVS.items() if p.exists()} or {
    f"{sys.version_info[0]}.{sys.version_info[1]}": sys.executable}
ok = True
for version, python in PYTHONS.items():
    with tempfile.TemporaryDirectory() as tmp:
        out = subprocess.run([python, DATA / "make_data.py"], cwd=tmp,
                             capture_output=True, text=True)
        made = sorted(p.name for p in Path(tmp).glob("*.csv"))
        kept = sorted(p.name for p in DATA.glob("*.csv"))
        same = made == kept and all(
            filecmp.cmp(Path(tmp) / n, DATA / n, shallow=False) for n in kept)
        same &= out.stdout == (DATA / "make_data.out").read_text()
    ok &= same
    print(f"Python {version}: {'identical' if same else 'DIFFERENT'} ({len(made)} files)")
sys.exit(0 if ok else 1)
