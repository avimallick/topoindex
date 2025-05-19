import networkx as nx
from topoindex.utils.smiles_to_nx import smiles_to_nx

def eccentric_connectivity_index(smiles: str) -> int:
    G = smiles_to_nx(smiles)
    ecc = nx.eccentricity(G)
    return sum(G.degree[v] * ecc[v] for v in G.nodes())
