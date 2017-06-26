#!usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'youngilkim = youngilkim.check_date:main',
]

setup(
    name='youngilkim',
    version='0.0.3',
    description='example package',
    author='youngilkim',
    author_email='youngilkim@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)