# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='blazon',
    version='0.1.0',
    python_requires='==3.*,>=3.7.0',
    author='Brantley Harris',
    author_email='deadwisdom@gmail.com',
    packages=['blazon', 'blazon.constraints', 'blazon.environments'],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'inflection==0.*,>=0.3.1', 'pyyaml==5.*,>=5.3.1',
        'rfc3987==1.*,>=1.3.0', 'shortuuid==1.*,>=1.0.1'
    ],
    extras_require={
        "dev": [
            "black==19.*,>=19.10.0.b0", "fastjsonschema==2.*,>=2.14.4",
            "jsonschema==3.*,>=3.2.0", "pytest==3.*,>=3.0.0",
            "pytest-benchmark==3.*,>=3.2.3", "pytest-cov==2.*,>=2.7.0"
        ]
    },
)
