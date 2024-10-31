from setuptools import setup, find_packages

setup(
    name = 'myPackage',
    version = '0.1',
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'example python package',
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'https://github.com/gehadkamel/<package_name>',
    author = 'gehadkamel',
    author_email= 'gehad5kamel'

)