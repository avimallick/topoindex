# 🧠 TopoIndex

**TopoIndex** is a Python library for computing topological indices of molecular and graph structures using [NetworkX](https://networkx.org/) and [RDKit](https://www.rdkit.org/). It supports input via SMILES strings and is designed for mathematical chemistry, cheminformatics, and graph theory applications.

---

## 📦 Features

- ✅ **Wiener Index**
- ✅ **Zagreb Indices (First & Second)**
- ✅ **Hyper-Wiener Index**
- ✅ **Randic Index**
- ✅ **Balaban Index**
- ✅ **Eccentric Connectivity Index**
- ✅ **Graph Invariants**  
  - Node & edge count, diameter, radius, girth  
  - Spectral radius, Estrada index, Graph energy  
  - Optional distance matrix output
- ✅ **Command-Line Interface (CLI)**
- 📘 More indices coming soon!

---

## 🚀 Installation

Once released on PyPI:

```bash
pip install topoindex
```

For manual installation:

```bash
git clone https://github.com/avimallick/topoindex.git
cd topoindex
pip install -e .
```

> ⚠️ Requires `networkx`, `rdkit` and `pandas`.

---

## 🧪 Example Usage (Python)

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
from topoindex.graphs.invariants import compute_invariants

smiles = "CCO"  # Ethanol

print("Wiener:", wiener_index(smiles))
print("Zagreb-1:", first_zagreb_index(smiles))
print("Zagreb-2:", second_zagreb_index(smiles))
print("Hyper-Wiener:", hyper_wiener_index(smiles))
print("Randic:", randic_index(smiles))
print("Balaban:", balaban_index(smiles))
print("Eccentric Connectivity:", eccentric_connectivity_index(smiles))

invariants = compute_invariants(smiles, include_matrix=True, matrix_format="pandas")
print("Graph Invariants:", invariants)
```

---

## 🖥️ CLI Usage

TopoIndex also provides a command-line interface:

```bash
topoindex --smiles "C1=CC=CC=C1" --matrix --matrix-format pandas
```

Example Output (JSON):

```json
{
  "num_nodes": 6,
  "num_edges": 6,
  "diameter": 3,
  "radius": 3,
  "girth": 6,
  "spectral_radius": 2.0,
  "estrada_index": 9.38,
  "graph_energy": 8.47,
  "distance_matrix": [[0, 1, 2, 1, 2, 3], [1, 0, 1, 2, 3, 2], ...]
}
```

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