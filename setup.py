"""
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

Parameters:

    * `bin`: Path to script file. Default is currently running script file
    * `base`: Name of base module directory to add to sys.path. Default is "lib".
    * `append`: Append module directory to the end of sys.path, or insert at the beginning? Default is to append.
    * `ignore`: List of directories to ignore during the module search. Default is to ignore "/" and "/usr".
    * `realpath`: Should symlinks be resolved first? Default is False.
    * `pythonpath`: Should the modules directory be added to the PYTHONPATH environment variable? Default is False.
    * `throw`: Should an exception be thrown if no modules directory was found? Default is False.
"""

from setuptools import setup

setup(
    name='findmodules',
    version='0.1',
    description='Find project module directory relative to the running script',
    url='https://github.com/benwbooth/python-findmodules',
    author='Ben Booth',
    author_email='benwbooth@gmail.com',
    license='MIT',
    keywords="python module import directory path location folder",
    zip_safe=True,
    description=__doc__)
