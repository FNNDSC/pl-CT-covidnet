from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             =   'ct_covidnet',
    version          =   '0.2.0',
    description      =   'Use COVID-Net prediction on CT scan.',
    long_description =   readme,
    author           =   'DarwinAI',
    author_email     =   'jeffer.peng@darwinai.ca',
    url              =   'https://github.com/FNNDSC/pl-CT-covidnet',
    packages         =   ['ct_covidnet'],
    install_requires =   ['chrisapp'],
    license          =   'AGPL-3.0',
    zip_safe         =   False,
    entry_points     = {
        'console_scripts': [
            'ct_covidnet = ct_covidnet.__main__:main'
            ]
        }
)
