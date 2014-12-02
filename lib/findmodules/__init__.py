"""
findmodules
===========

Find project module directory relative to the running script.

This module will search the currently runnings script's parent directory, and
all successive parent directories up to the root directory for a module matching
the `base` argument. If found, the directory is added to sys.path.

This is useful for sets of scripts that use custom project-specific modules that
you don't want to install into the system python modules folders.

Example usage::

    import findmodules
    findmodules.init(base='modules', realpath=True)

This example will search for a folder called "modules" in the current script's
directory, and all parent directories. Symlinks will be resolved first. If the
directory is found, it will be appended to sys.path.
"""

import os, os.path, sys

def init(bin=sys.argv[0], base='lib', append=True, ignore=['/','/usr'], realpath=False, pythonpath=False):
    """
    Parameters:
    * `bin`: Path to script file. Default is currently running script file
    * `base`: Name of base module directory to add to sys.path. Default is "lib".
    * `append`: Append module directory to the end of sys.path, or insert at the beginning? Default is to append.
    * `ignore`: List of directories to ignore during the module search. Default is to ignore "/" and "/usr".
    * `realpath`: Should symlinks be resolved first? Default is True.
    * `pythonpath`: Should the modules directory be added to the PYTHONPATH environment variable? Default is False.
    """
    if type(ignore) is str: ignore = [ignore]
    bin = os.realpath(bin) if realpath else os.path.abspath(bin)
    path = os.path.dirname(bin)

    while os.path.dirname(path) != path and (path in ignore or not os.path.isdir(os.path.join(path, base))):
        path = os.path.dirname(path)

    if path not in ignore and os.path.isdir(os.path.join(path, base)):
        if append: sys.path.append(os.path.join(path, base))
        else: sys.path.insert(1, os.path.join(path, base))

        if pythonpath:
            os.environ['PYTHONPATH'] = '' if 'PYTHONPATH' not in os.environ
            os.environ['PYTHONPATH'] += os.path.join(path, base) if not append
            os.environ['PYTHONPATH'] += os.pathsep if os.environ['PYTHONPATH'] != ''
            os.environ['PYTHONPATH'] += os.path.join(path, base) if append
