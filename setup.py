from setuptools import setup, find_packages

setup(
    name="topoindex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "networkx",
        #"rdkit-pypi",
    ],
    author="Avinash Mallick",
    description="A Python library for computing topological indices from SMILES using NetworkX",
    license="MIT",
)
