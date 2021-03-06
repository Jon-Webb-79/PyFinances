# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='PyFinances',
        version='0.1.0',
        description='develops a statistical estimate for the value of checking and savings account',
        long_description=readme,
        author='Jonathan A. Webb',
        author_email='webbja123@gmail.com',
        license=license,
        packages=find_packages(),
        classifiers=[
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: BSD License"
            "Programming Language :: Python :: 3",
            "Programming Languate :: Python :: 3.9", 
            "Operating System :: MacOS",
        ],
        zip_safe=False,
)
