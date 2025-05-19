import math
from topoindex.utils.smiles_to_nx import smiles_to_nx

def balaban_index(smiles: str) -> float:
    G = smiles_to_nx(smiles)
    m = G.number_of_edges()
    n = G.number_of_nodes()
    mu = m - n + 1  # cyclomatic number
    if mu == -1: return 0.0  # avoid division by zero
    numerator = sum(1 / math.sqrt(G.degree[u] * G.degree[v]) for u, v in G.edges())
    return (m / (mu + 1)) * numerator
