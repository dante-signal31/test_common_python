import os
from setuptools import setup, find_packages  # Always prefer setuptools over distutilss


VDIST_PACKAGES_CONFIG = "packaging/coko_vdist.cnf"

LONG_DESCRIPTION = """In this package you can find some functions I use frequently at my tests.

## Modules list
### fs 
Filesystem utilities. They are useful to prepare folders and files for your tests.
#### crypto
Cryptographic functions for your tests. Here you can find hashing functions to check file contents.
#### tmp
Functions to create temporal folder and files.
#### ops
Functions for file operations (copy, delete, etc).

More info in: https://github.com/dante-signal31/test_common_python
"""


def find_folders_with_this_name(dir_name: str) -> str:
    """ Look for folder with given name, searching from current working dir.

    :param dir_name: Folder name to look for.
    :return: Relative path, from current working dir, where folder is.
    """
    for dir, dirs, files in os.walk('.'):
        if dir_name in dirs:
            yield os.path.relpath(os.path.join(dir, dir_name))


setup(name="test_common",
      version="0.1.0",
      description="Common functions useful for tests.",
      long_description=LONG_DESCRIPTION,
      author="Dante Signal31",
      author_email="dante.signal31@gmail.com",
      license="BSD-3",
      url="https://github.com/dante-signal31/test_common_python",
      download_url="https://github.com/dante-signal31/coko/releases",
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Other Audience',
                   'Topic :: System',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.7'],
      keywords="test",
      install_requires=[],
      zip_safe=False,
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                      "tests", "*tests*", "ci_scripts",
                                      "ci_scripts.*", "*.ci_scripts",
                                      "*.ci_scripts.*", "*ci_scripts*",
                                      "ci_scripts*"]),
      )