# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='erpnextloyaltyapp',
    version=version,
    description='The app is used to give loyalty points to the users based on various Rules',
    author='New Indictrans Technologies PVT LTD',
    author_email='ravindra.l@indictranstech.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
