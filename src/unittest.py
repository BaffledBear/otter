from functools import wraps


class TestCase(object):
    """
    A test case is a single, minimal amount of work. This class provides a
    decorator that can be used on a test case method. The method will be
    wrapped by this class and the methods defined here. These methods should be
    defined in a child of the UnitTest class.
    """

    testList = []

    def __init__(self, f):
        self.func = f
        self.__name__ = f.__name__
        self.register_test(f)

    def __call__(self):
        """Defines the behavior when the method is called."""
        self.func()

    def clear_test_list():
        """Empties the test list for use in a new UnitTest."""
        TestCase.testList.clear()

    def register_test(self, f):
        """Adds the test case to the list of items to be tested."""
        self.testList.append({"name": f.__name__, "func": f})

    @staticmethod
    def expected_failure(func):
        @wraps(func)
        def wrapper(self):
            if func.__name__ not in self.expectedFailList:
                self.expectedFailList.append(func.__name__)
            func(self)
        return wrapper


class UnitTest(object):
    """
    Base class to be inherited when creating a new unit test. Provides set_up
    and tear_down methods to be overridden. As well as a get_test_list() method
    which will return the list of tests being used by the current instance.
    """

    def __init__(self):
        """
        Initialize the instance. Get a copy of the test list from TestCase.
        Clear the static value of TestCase.testList so the next class can use
        it.
        """
        self.expectedFailList = []
        self.testList = TestCase.testList.copy()
        TestCase.clear_test_list()

    def set_up(self):
        """If this is not overridden, a message will print."""
        print("set_up() not overridden.")

    def get_test_list(self):
        """Return the instances test list."""
        return self.testList

    def tear_down(self):
        """If this is not overridden, a message will print."""
        print("tear_down() not overridden.")
