from typing import Dict, Optional, Literal, Union
import numpy as np
import networkx as nx
from rdkit import Chem
from rdkit.Chem import rdmolops

from topoindex.utils.graph_utils import mol_to_nx


def compute_invariants(
    smiles: str,
    include_matrix: bool = False,
    matrix_format: Literal["numpy", "pandas"] = "numpy"
) -> Dict[str, Union[int, float, np.ndarray]]:
    """
    Compute basic graph invariants from a SMILES string.

    Parameters:
        smiles (str): Input molecule in SMILES format.
        include_matrix (bool): If True, includes the distance matrix.
        matrix_format (str): Format of distance matrix ('numpy' or 'pandas').

    Returns:
        Dict[str, Union[int, float, np.ndarray]]: Graph invariant values.
    """
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid SMILES string.")

    G = mol_to_nx(mol)
    n_nodes = G.number_of_nodes()
    n_edges = G.number_of_edges()

    result = {
        "num_nodes": n_nodes,
        "num_edges": n_edges,
        "diameter": nx.diameter(G) if nx.is_connected(G) else -1,
        "radius": nx.radius(G) if nx.is_connected(G) else -1,
        "girth": girth(G),
        "spectral_radius": spectral_radius(G),
        "estrada_index": nx.estrada_index(G),
        "graph_energy": graph_energy(G)
    }

    if include_matrix:
        dist = dict(nx.all_pairs_shortest_path_length(G))
        matrix = np.zeros((n_nodes, n_nodes), dtype=int)
        for i, row in dist.items():
            for j, d in row.items():
                matrix[i][j] = d
        result["distance_matrix"] = matrix if matrix_format == "numpy" else to_pandas(matrix)

    return result


def girth(G: nx.Graph) -> int:
    try:
        cycles = nx.minimum_cycle_basis(G)
        return min(len(c) for c in cycles) if cycles else -1
    except:
        return -1


def spectral_radius(G: nx.Graph) -> float:
    A = nx.to_numpy_array(G)
    eigenvalues = np.linalg.eigvals(A)
    return max(np.abs(eigenvalues))


def graph_energy(G: nx.Graph) -> float:
    A = nx.to_numpy_array(G)
    eigenvalues = np.linalg.eigvals(A)
    return float(np.sum(np.abs(eigenvalues)))


def to_pandas(matrix: np.ndarray):
    import pandas as pd
    return pd.DataFrame(matrix)
