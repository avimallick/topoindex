from topoindex.indices.wiener import wiener_index
from topoindex.indices.zagreb import first_zagreb_index, second_zagreb_index
from topoindex.indices.hyper_wiener import hyper_wiener_index
from topoindex.indices.randic import randic_index
from topoindex.indices.balaban import balaban_index
from topoindex.indices.eccentric_connectivity import eccentric_connectivity_index

smiles = "CCO"  # ethanol

print("Wiener:", wiener_index(smiles))
print("Zagreb-1:", first_zagreb_index(smiles))
print("Zagreb-2:", second_zagreb_index(smiles))
print("Hyper-Wiener:", hyper_wiener_index(smiles))
print("Randic:", randic_index(smiles))
print("Balaban:", balaban_index(smiles))
print("Eccentric Connectivity:", eccentric_connectivity_index(smiles))
