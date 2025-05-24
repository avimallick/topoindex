import networkx as nx
from rdkit.Chem import rdmolops

def mol_to_nx(mol):
    return nx.Graph(rdmolops.GetAdjacencyMatrix(mol))
