import setuptools, os
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as doc:
    __doc__=doc.read()

setuptools.setup(
    name='findmodules',
    version='0.6',
    url='https://github.com/benwbooth/python-findmodules',
    author='Ben Booth',
    author_email='benwbooth@gmail.com',
    license='MIT',
    keywords="python module import directory path location folder",
    zip_safe=True,
    description='Find project module directory relative to the running script.',
    py_modules=['findmodules'])
