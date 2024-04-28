import os
import shutil
import subprocess

from Cython.Build import cythonize
from setuptools import setup
from setuptools.command.build_ext import build_ext


class CustomBuildExt(build_ext):
  """Custom build_ext command to run stubgen after building Cython extensions."""

  def run(self):
    # 编译完成后，运行 stubgen 来生成 .pyi 文件
    module_path = 'object_storage'
    stub_dir = '.types'
    subprocess.run(['stubgen', '-o', stub_dir, '-p', module_path])
    generated_stub_dir = os.path.join(stub_dir, module_path)
    shutil.copytree(generated_stub_dir, module_path, dirs_exist_ok=True)
    # 运行原始的 build_ext 命令来编译 Cython 代码
    super().run()


setup(
  name='object-storage',
  ext_modules=cythonize('object_storage/*.py'),
  cmdclass={
    'build_ext': CustomBuildExt,
  },
  script_args=['build_ext', '--inplace'],
)
