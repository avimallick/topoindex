import math
from topoindex.utils.smiles_to_nx import smiles_to_nx

def randic_index(smiles: str) -> float:
    G = smiles_to_nx(smiles)
    return sum(1 / math.sqrt(G.degree[u] * G.degree[v]) for u, v in G.edges())
