from importlib import import_module
from inspect import isclass
from pathlib import Path
from pkgutil import iter_modules

# A bit of copy/pasta to automatically import all files in this subdirectory.
# This automatically resolves all subcalsses of BaseExecutor
package_dir = Path(__file__).resolve().parent
if package_dir:
    for (_, module_name, _) in iter_modules([package_dir.as_posix()]):

        # import the module and iterate through its attributes
        module = import_module(f"{__name__}.{module_name}")
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)

            if isclass(attribute):
                # Add the class to this package's variables
                globals()[attribute_name] = attribute
