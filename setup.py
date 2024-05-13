from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="lib-version",
    version='0.0.1',
    url='https://github.com/remla24-team8/lib-version',
    author='Sayf el Kaddouri',
    description='A version-aware library that can can be asked for the version of the library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['utility', 'versioning'],
)