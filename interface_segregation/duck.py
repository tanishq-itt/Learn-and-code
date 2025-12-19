from flyable import Flyable
from swimable import Swimable

class Duck(Flyable, Swimable):
    def fly(self):
        print("Duck flying")

    def swim(self):
        print("Duck swimming")
