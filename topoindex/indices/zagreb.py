import networkx as nx
from topoindex.utils.smiles_to_nx import smiles_to_nx

def first_zagreb_index(smiles: str) -> int:
    G = smiles_to_nx(smiles)
    return sum(d**2 for _, d in G.degree())

def second_zagreb_index(smiles: str) -> int:
    G = smiles_to_nx(smiles)
    return sum(G.degree(u) * G.degree(v) for u, v in G.edges())
