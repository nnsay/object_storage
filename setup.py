from setuptools import setup
from Cython.Build import cythonize

setup(
    name="object_storage",
    version="0.1",
    ext_modules=cythonize("object_storage/example.py"),
    package_dir={"": "object_storage"},
    package_data={
        "object_storage": [
            "*.so",
        ]
    },  # 确保 .so 文件被包括
    include_package_data=True,
    zip_safe=False,
)
