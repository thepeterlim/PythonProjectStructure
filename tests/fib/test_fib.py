from helloworld.fib.fibinacci import get_fibonacci_seq


def test_fib():
    index = 18
    expected = 2584
    actual = get_fibonacci_seq(index)
    assert expected == actual


def test_fib():
    index = 23
    expected = 28657
    actual = get_fibonacci_seq(index)
    assert expected == actual
