from setuptools import setup, find_packages

setup(
    name="object_storage",
    version="0.1",
    packages=find_packages(),
    package_data={"object_storage": ["object_storage/**/*.so"]},
)
