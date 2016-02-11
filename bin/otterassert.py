"""Assert defines the Assert methods and the behaviors that are used by them."""
class OtterAssert:

    __successCount = 0
    __failCount = 0
    __passedTests = []
    __failedTests = []


    def __init__(self):
        pass

    ## TODO - Update comments for docstring use
    """Checks whether the argument is the boolean value True."""
    def assertTrue(self, statusBool, testCase):
        if statusBool:
            self.__successCount += 1
            self.__logSuccess(testCase)
        else:
            self.__failCount += 1
            self.__logFail(testCase)


    """Checks for equality of the two arguments."""
    assertEqual(self, expected, actual):
        pass


    """Checks for inequality of the two arguments."""
    assertNotEqual(self, expected, actual):
        pass


    """Checks whether the argument is the boolean value False."""
    assertFalse(self, expected):
        pass


    """Checks whether the argument is in the collection."""
    assertIn(self, expected, collection):
        pass


    """Checks whether the argument is not in the collection."""
    assertNotIn(self, expected, collection):
        pass


    """Checks whether the value is the expected."""
    assertIs(self, expected, actual):
        pass


    """Checks whether the value is not the expected."""
    assertIsNot(self, expected, actual):
        pass


    """Checks whether the argument is None."""
    assertIsNone(self, expected):
        pass


    """Checks whether the argument is not None."""
    assertIsNotNone(self, expected):
        pass


    """Checks whether the function 'func' raises an exception of the type 'exception'."""
    assertRaises(self, exception, func, *args):
        pass


    def __logSuccess(self, testCase):
        self.__passedTests.append(testCase)


    def __logFail(self, testCase):
        self.__failedTests.append(testCase)

    ## TODO - Move to Otter class and replace here with getters
    def printResults(self):
        print("Number of Successes: {}".format(self.__successCount))
        for case in self.__passedTests:
            print("\t{}".format(case))
        print("")
        print("Number of Failures:  {}".format(self.__failCount))
        for case in self.__failedTests:
            print("\t{}".format(case))
