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
    assertEqual(expected, actual):
        pass


    """Checks for inequality of the two arguments."""
    assertNotEqual(expected, actual):
        pass


    """Checks whether the argument is the boolean value False."""
    assertFalse(expected):
        pass


    """Checks whether the argument is in the collection."""
    assertIn(expected, collection):
        pass


    """Checks whether the argument is not in the collection."""
    assertNotIn(expected, collection):
        pass


    """Checks whether the value is the expected."""
    assertIs(expected, actual):
        pass


    """Checks whether the value is not the expected."""
    assertIsNot(expected, actual):
        pass


    """Checks whether the argument is None."""
    assertIsNone(expected):
        pass


    """Checks whether the argument is not None."""
    assertIsNotNone(expected):
        pass


    """Checks whether the function 'func' raises an exception of the type 'exception'."""
    assertRaises(exception, func, *args):
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
