from rdkit import Chem
import networkx as nx

def smiles_to_nx(smiles: str) -> nx.Graph:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")

    G = nx.Graph()
    for atom in mol.GetAtoms():
        G.add_node(atom.GetIdx(), symbol=atom.GetSymbol())

    for bond in mol.GetBonds():
        G.add_edge(bond.GetBeginAtomIdx(), bond.GetEndAtomIdx())

    return G
