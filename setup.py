from setuptools import setup, find_packages

setup(
    name='fastxfourier-site',
    version='0.1.0',
    packages=find_packages(exclude=('tests', 'site')),
    include_package_data=True,
)
