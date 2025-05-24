import argparse
import json
from topoindex.graphs.invariants import compute_invariants

def main():
    parser = argparse.ArgumentParser(description="Compute topological invariants from SMILES")
    parser.add_argument("--smiles", type=str, required=True, help="Input SMILES string")
    parser.add_argument("--matrix", action="store_true", help="Include distance matrix")
    parser.add_argument("--matrix-format", type=str, choices=["numpy", "pandas"], default="numpy")

    args = parser.parse_args()
    result = compute_invariants(
        smiles=args.smiles,
        include_matrix=args.matrix,
        matrix_format=args.matrix_format
    )

    # Convert numpy/pandas to list for JSON printing
    if "distance_matrix" in result:
        dm = result["distance_matrix"]
        if hasattr(dm, "values"):  # it's a DataFrame
            result["distance_matrix"] = dm.values.tolist()
        else:  # it's a NumPy array
            result["distance_matrix"] = dm.tolist()


    print(json.dumps(result, indent=2))
