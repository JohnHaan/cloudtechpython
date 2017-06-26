#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'dolbam = dolbam.check_date:main',
]

setup(
    name='dolbam',
    version='0.0.2',
    description='example package',
    author='dolbam',
    author_email='dolbam@netmarble.com',
    url='https://example.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
