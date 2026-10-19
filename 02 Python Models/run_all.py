"""Run every model in order and rebuild all charts and tables in ../outputs."""
import runpy, pathlib
here = pathlib.Path(__file__).parent
for m in sorted(here.glob("model_[0-9][0-9]_*.py")):
    print(f"\n==== {m.name} ====")
    runpy.run_path(str(m), run_name="__main__")
