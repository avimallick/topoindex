from topoindex.indices.wiener import wiener_index

def test_wiener_index_ethanol():
    assert wiener_index("CCO") == 4