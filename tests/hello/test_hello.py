from helloworld.hello.hello import add_stuff


def test_add_stuff():
    expected = 8
    actual = add_stuff(3, 5)
    assert actual == expected

