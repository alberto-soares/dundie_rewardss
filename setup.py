# setuptools

# from setuptools import setup  so os pacotes dentro de dundie
from setuptools import setup, find_packages # sub pacotes 

setup(
    name="dundie",

#   SEMANTIC VERSIONING
#            |-------> x MAJOR
#            | |-----> y MINOR
#            | | |---> z PATCH
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Alberto Santos",
#    packages=["dundie"]  só os pacotes dentro de dundie
    packages=find_packages(),
)

# pyproject

# external build tools (poetry, flit & outros)
