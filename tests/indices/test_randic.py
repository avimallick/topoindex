from topoindex import randic_index

def test_randic_ethanol():
    result = randic_index("CCO")
    assert abs(result - 1.4142) < 0.001
