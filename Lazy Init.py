from inspect import signature


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        result = type.__new__(mcs, name, bases, namespace)
        keys = (namespace.keys())

    def lazy_init(self, *args):


class A:
    def __init__(self, arg1, arg2, arg3):
        pass


a = A(1, 2, 3)
print(signature(A).parameters)
