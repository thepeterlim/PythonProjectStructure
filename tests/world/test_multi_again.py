from helloworld.world.world import mult


def test_multi_again():
    expected = 110
    actual = mult(11, 10)
    assert expected == actual
