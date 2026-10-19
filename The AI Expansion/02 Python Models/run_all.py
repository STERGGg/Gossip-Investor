"""Runs every model in order, rebuilding all charts and tables in 04 Outputs. The two cartoons in 04 Outputs/comics are drawn images and are not generated here."""
import runpy
from pathlib import Path
here = Path(__file__).parent
scripts = sorted(here.glob("model_[0-9][0-9]_*.py"))
for m in scripts:
    print("running", m.name)
    runpy.run_path(str(m), run_name="__main__")
