from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:

    ''' This Functin will return list of requirements'''

    requirements_list:list[str] = []

    ''' Write the code to read the requirements.txt file and append each requirement_list variable.'''
    return requirements_list

setup(
    name="sensor",
    version="0.0.1",
    author="Zaid",
    author_email="zaid_zeee28@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements(),
)