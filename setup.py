from setuptools import setup, find_packages

setup(
    name='mediadilutor',
    version='0.1',
    packages=find_packages(where='src'),
    url='https://github.com/bk1n/media-dilutor',
    author='Ben King',
    description='Package to calculate dilutions',
    package_dir={'': 'src'}
)