def get_fibonacci_seq(index):
    if index == 0:
        return 0
    if index == 1:
        return 1

    return get_fibonacci_seq(index - 1) + get_fibonacci_seq(index - 2)
