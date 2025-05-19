from setuptools import setup, find_packages

setup(
    name="topoindex",
    version="0.1.5",
    packages=find_packages(),
    install_requires=["networkx", "rdkit"],
    author="Avinash Mallick",
    author_email="avimallick@gmail.com",
    description="A Python library for computing topological indices from SMILES using NetworkX",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/avimallick/topoindex",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
