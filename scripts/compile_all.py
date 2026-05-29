import py_compile
from pathlib import Path
import sys

files = list(Path('.').rglob('*.py'))
errors = 0
for f in files:
    try:
        py_compile.compile(str(f), doraise=True)
    except Exception as e:
        print('ERROR', f, e)
        errors += 1

print('Files checked:', len(files))
print('Errors:', errors)
if errors:
    sys.exit(1)
