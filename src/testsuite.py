from functools import wraps


class TestCase(object):

    testList = []

    def __init__(self, f):
        self.func = f
        self.__name__ = f.__name__
        self.register_test(f)

    def __call__(self):
        self.func()

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        new_func = self.func.__get__(obj, type)
        return self.__class__(new_func)

    def register_test(self, f):
        self.testList.append({"name": f.__name__, "func": f})

    @staticmethod
    def expected_failure(func):
        @wraps(func)
        def wrapper(self):
            if func.__name__ not in self.expectedFailList:
                self.expectedFailList.append(func.__name__)
            func(self)
        return wrapper


class TestSuite(object):

    def __init__(self):
        self.expectedFailList = []
        self.testList = TestCase.testList
        self.set_up()

    def set_up(self):
        print("set_up() not overridden.")

    def get_test_list(self):
        return self.testList

    def tear_down(self):
        print("tear_down() not overridden.")

