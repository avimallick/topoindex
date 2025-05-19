import networkx as nx
from topoindex.utils.smiles_to_nx import smiles_to_nx

def wiener_index(smiles: str) -> int:
    G = smiles_to_nx(smiles)
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    total = 0
    for u in path_lengths:
        for v in path_lengths[u]:
            if u < v:
                total += path_lengths[u][v]
    return total
