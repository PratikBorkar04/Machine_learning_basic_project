from setuptools import setup
from typing import List


PROJECT_NAME = "housing Predictor"
VERSION = "0.0.1"
AUTHOR = "Pratik"
DESCRIPTION = "First fully working machine learning project"
PACKAGES = ['housing']
REQUIREMENTS_FILE_NAME = 'requirements.txt'


def get_requirements_list()->List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_file.readlines()


setup (
name = PROJECT_NAME ,
version = VERSION ,
author = AUTHOR ,
description = DESCRIPTION ,
packages = PACKAGES ,
install_requires =  get_requirements_list()
)
