import pytest
from topoindex.graphs.invariants import compute_invariants


def test_benzene_invariants():
    benzene = "C1=CC=CC=C1"
    result = compute_invariants(benzene)

    assert result["num_nodes"] == 6
    assert result["num_edges"] == 6
    assert result["diameter"] == 3
    assert result["radius"] == 3
    assert result["girth"] == 6
    assert "spectral_radius" in result
    assert "estrada_index" in result
    assert "graph_energy" in result


def test_invalid_smiles():
    with pytest.raises(ValueError):
        compute_invariants("notasmiles")


def test_distance_matrix_output():
    propane = "CCC"
    result = compute_invariants(propane, include_matrix=True, matrix_format="numpy")
    assert "distance_matrix" in result
    assert result["distance_matrix"].shape == (3, 3)
