from functools import wraps


def say_hello():
    print("Hello!")


def add_stuff(item1: int, item2: int) -> int:
    return item1 + item2


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    """say stuff"""
    msg = "Can you buy me a beer?"
    return msg, say_please
