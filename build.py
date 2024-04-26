from Cython.Build import cythonize
from setuptools import setup

setup(
  name='nnsay.object-storage',
  ext_modules=cythonize('object_storage/object_storage.py'),
  script_args=['build_ext', '--inplace'],
)
