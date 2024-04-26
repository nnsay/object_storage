from setuptools import setup
from Cython.Build import cythonize

setup(
    name="object_storage",
    version="0.1",
    description="smart file object operation library",
    author="Jimmy Wang",
    author_email="jimmy.w@aliyun.com",
    url="https://github.com/nnsay/object_storage",
    ext_modules=cythonize("object_storage/*.py"),
    package_dir={"": "object_storage"},
    package_data={
        "object_storage": [
            "*.so",
        ]
    },  # 确保 .so 文件被包括
    include_package_data=True,
    zip_safe=False,
)
