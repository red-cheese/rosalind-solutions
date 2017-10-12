import os
import types
from importlib import machinery


cur_dir = os.path.dirname(__file__)
for path in os.listdir(cur_dir):
    if path.endswith('.py') and not path.startswith('_'):
        loader = machinery.SourceFileLoader(path[:-3], os.path.join(cur_dir, path))
        mod = types.ModuleType(loader.name)
        loader.exec_module(mod)

        # To allow statements like 'from impl import <name>'
        globals()[loader.name] = mod
