from topoindex.indices.balaban import balaban_index

def test_balaban_ethanol():
    result = balaban_index("CCO")
    assert abs(result - 2.8284) < 0.001
