from pprint import pprint


class BaseClass:
    base_Calls = 0

    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def call_me(self):
        self.base_Calls += 1
        print('calling Base class')


class LeftClass(BaseClass):
    left_calls = 0

    def __init__(self, c, *args):
        super().__init__(*args)
        self.c = c

    def call_me(self):
        super().call_me()
        self.left_calls += 1
        print('caliing left class')


class RightClass(BaseClass):
    right_calls = 0

    def __init__(self, d, e, f, *args):
        super().__init__(*args)
        self.d = d
        self.e = e
        self.f = f

    def call_me(self):
        super().call_me()
        self.right_calls += 1
        print('calling right class')


class SubClass(LeftClass, RightClass):
    sub_calls = 0

    def __init__(self, g, *args):
        super().__init__(*args)
        self.g = g

    def call_me(self):
        super().call_me()
        self.sub_calls += 1
        print('calling sub class')


