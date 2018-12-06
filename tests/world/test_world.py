from helloworld.world.world import mult


def test_mult():
    assert mult(3, 5) == 15


def test_add_stuff2():
    expected = 36
    actual = mult(12, 3)
    assert actual == expected
