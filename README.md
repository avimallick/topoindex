# TopoIndex

A Python library for computing topological indices of graphs using NetworkX.

## Features

- Wiener Index
- Zagreb Index (coming soon)
- Randic Index (coming soon)

## Install

```bash
pip install topoindex  # (after PyPI release)


### 🔖 4. Add MIT License

Create a `LICENSE` file and paste in the [MIT License text](https://opensource.org/licenses/MIT).

---

## 🔧 5. Add Basic `setup.py` and `pyproject.toml`

### `setup.py`:
```python
from setuptools import setup, find_packages

setup(
    name="topoindex",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["networkx"],
    author="Your Name",
    description="A Python library for graph topological indices.",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)

