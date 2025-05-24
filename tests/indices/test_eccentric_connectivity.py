from topoindex import eccentric_connectivity_index

def test_eccentric_connectivity_ethanol():
    assert eccentric_connectivity_index("CCO") == 6
