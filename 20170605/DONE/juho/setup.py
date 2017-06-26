#!/usr/bin/env python
#!/usr/bin/env python

from setuptools import setup, find_packages

console_scripts = [
    'juho_what_year = juho.check_date:year',
    'juho_what_month = juho.check_date:month',
    'juho_what_date = juho.check_date:date',
    'juho_what_time = juho.check_date:time',
]

setup(
    name='juho',
    version='0.0.1',
    description='example package',
    author='Juho Son',
    author_email='harry2853@netmarble.com',
    url='https://masterson.com',
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={'console_scripts': console_scripts},
)
