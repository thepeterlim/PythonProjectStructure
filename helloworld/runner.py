import helloworld.hello.hello as hello
import helloworld.world.world as world
import helloworld.whatup as whatup
from helloworld.hello.hello import say

if __name__ == "__main__":
    hello.say_hello()
    world.say_world()
    whatup.say_what_up()

    # Shows how wrapper decorator works
    # in beg function.  If @wrapper wasn't used
    # __name__ would say wrapper
    # and help(say) would give description of wrapper function
    # but would ignore the docstring on actually say function
    print(say.__name__)
    print(help(say))
    print(say(say_please=True))
