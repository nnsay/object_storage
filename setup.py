from setuptools import setup, find_packages

setup(
    name="object_storage",
    version="0.1",
    packages=find_packages(),  # 表示当前目录作为根包
    package_data={
        "object_storage": ["object_storage/object_storage.so"]
    },  # 确保 .so 文件被包括
    include_package_data=True,
)
