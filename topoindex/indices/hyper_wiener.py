import networkx as nx
from topoindex.utils.smiles_to_nx import smiles_to_nx

def hyper_wiener_index(smiles: str) -> float:
    G = smiles_to_nx(smiles)
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    total = 0
    for u in path_lengths:
        for v in path_lengths[u]:
            if u < v:
                d = path_lengths[u][v]
                total += d + d**2
    return 0.5 * total
