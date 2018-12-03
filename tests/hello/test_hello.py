from helloworld.hello.hello import add_stuff


def test_add_stuff():
    assert add_stuff(3, 5) == 8
