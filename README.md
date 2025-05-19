# 🧠 TopoIndex

**TopoIndex** is a Python library for computing topological indices of molecular and graph structures using [NetworkX](https://networkx.org/). It supports input via SMILES strings and is designed for mathematical chemistry, cheminformatics, and graph theory applications.

---

## 📦 Features

- ✅ **Wiener Index**
- ✅ **Zagreb Indices (First & Second)**
- ✅ **Hyper-Wiener Index**
- ✅ **Randic Index**
- ✅ **Balaban Index**
- ✅ **Eccentric Connectivity Index**
- 📘 More indices coming soon!

---

## 🚀 Installation

Once released on PyPI:

```bash
pip install topoindex
```

For now (manual installation):

```bash
git clone https://github.com/avimallick/topoindex.git
cd topoindex
pip install .
```

> ⚠️ Requires `networkx`. RDKit must be installed separately via Conda:
> 
> ```bash
> conda install -c rdkit rdkit
> ```

---

## 🧪 Example Usage

```python
from topoindex import (
    wiener_index,
    first_zagreb_index,
    second_zagreb_index,
    hyper_wiener_index,
    randic_index,
    balaban_index,
    eccentric_connectivity_index,
)

smiles = "CCO"  # Ethanol

print("Wiener:", wiener_index(smiles))
print("Zagreb-1:", first_zagreb_index(smiles))
print("Zagreb-2:", second_zagreb_index(smiles))
print("Hyper-Wiener:", hyper_wiener_index(smiles))
print("Randic:", randic_index(smiles))
print("Balaban:", balaban_index(smiles))
print("Eccentric Connectivity:", eccentric_connectivity_index(smiles))


---

## 🧠 What are Topological Indices?

Topological indices are numerical descriptors of graph structure widely used in:

- Molecular property prediction
- Graph similarity comparison
- Cheminformatics and QSPR/QSAR
- Network analysis

---

## 📝 License

Licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome. If you'd like to contribute a new index or optimization, please open an issue first.

---

## 👨‍💻 Author

Developed by [Avinash Mallick](https://github.com/avimallick).
