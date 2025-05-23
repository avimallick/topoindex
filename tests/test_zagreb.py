from topoindex import first_zagreb_index, second_zagreb_index

def test_zagreb_indices_ethanol():
    assert first_zagreb_index("CCO") == 6
    assert second_zagreb_index("CCO") == 4
