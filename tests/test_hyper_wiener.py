from topoindex import hyper_wiener_index

def test_hyper_wiener_ethanol():
    assert hyper_wiener_index("CCO") == 5.0
