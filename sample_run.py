from topoindex import (
    wiener_index,
    first_zagreb_index,
    second_zagreb_index,
    hyper_wiener_index,
    randic_index,
    balaban_index,
    eccentric_connectivity_index,
)

smiles = "CCO"  # ethanol

print("Wiener:", wiener_index(smiles))
print("Zagreb-1:", first_zagreb_index(smiles))
print("Zagreb-2:", second_zagreb_index(smiles))
print("Hyper-Wiener:", hyper_wiener_index(smiles))
print("Randic:", randic_index(smiles))
print("Balaban:", balaban_index(smiles))
print("Eccentric Connectivity:", eccentric_connectivity_index(smiles))
