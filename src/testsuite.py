class TestSuite(object):

    def __init__(self):
        self.testList = self.TestCase.testList

    def set_up(self):
        print("set_up() not overridden.")

    class TestCase(object):

        testList = []
        
        def __init(self):
            pass

        def __init__(self, f):
            self.func = f
            self.__name__ = f.__name__
            self.register_test(f)

        def __call(self):
            self.func()

        def __get__(self, obj, type=None):
            if obj is None:
                return self
            new_func = self.func.__get__(obj, type)
            return self.__class__(new_func)

        def register_test(self, f):
            self.testList.append({"name": f.__name__, "func": f})

    def get_test_list(self):
        return self.testList

    def tear_down(self):
        print("tear_down() not overridden.")

    @TestCase
    def basic_test(self):
        print("I'm a test case!")

    @TestCase
    def basic_test_2(self):
        print("I'm a test case, too!")

