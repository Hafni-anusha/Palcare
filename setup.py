# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in palcare1/__init__.py
from palcare1 import __version__ as version

setup(
	name='palcare1',
	version=version,
	description='Palcare',
	author='Palcare',
	author_email='Palcare',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
