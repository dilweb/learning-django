import importlib, traceback

try:
    m = importlib.import_module('requestdataapp.forms')
    print('module imported OK, attrs:', [a for a in dir(m) if not a.startswith('_')])
except Exception:
    traceback.print_exc()
