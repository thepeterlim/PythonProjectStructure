import os
import sys
import helloworld.hello.hello as hello
import helloworld.world.world as world
import helloworld.whatup as whatup

if __name__ == "__main__":
    print(os.environ['PYTHONPATH'])
    print(sys.path)

    hello.say_hello()
    world.say_world()
    whatup.say_what_up()
