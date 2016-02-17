import sys
import traceback
from importlib import import_module
from src.asserts import OtterAssertError


class Otter(object):

    __successCount = 0
    __failCount = 0
    __passedTests = []
    __failedTests = []

    def __init__(self, testSuiteList):
        """
        testSuiteList should be a list of dictionaries. Key "module" should
        point to a string value of the location of a file with a TestSuite
        class. Key "class" should point to a string with the name of the class.
        """
        self.testSuiteInstanceList = []
        for suite in testSuiteList:
            self.append_test_suite_list(suite)

    def run(self):
        """
        Iterates through the instantiated list of TestSuites followed by their
        test cases and executes each case. Currently does not support arguments
        in the test cases. Setup and teardown methods are not called yet,
        either.
        """
        for suite in self.testSuiteInstanceList:
            for case in suite.get_test_list():
                self.execute_test(suite, case)
        self.print_results()

    def append_test_suite_list(self, suite):
        """
        Appends suite to the testSuiteInstanceList.
        """
        module = import_module(suite["module"])
        testSuite = getattr(module, suite["class"])
        self.testSuiteInstanceList.append(testSuite())

    def execute_test(self, suite, test_case):
        """
        Executes the function assigned in test_case and calls the proper log
        methods as needed. OtterAssertErrors are caught here. The flow should
        not break during any exceptions so generic exceptions are caught as and
        logged as well.
        """
        try:
            print("executing {}".format(test_case["name"]))
            test_case["func"](suite)
            print()
        except OtterAssertError as e:
            self.append_failed_test(
                {
                    "case": test_case["name"],
                    "message": e.args[0],
                    "trace": traceback.format_exc()
                }
            )
            self.increment_fail_count()
        except:
            traceback.print_exc(file=sys.stdout)
            self.append_failed_test(
                {
                    "case": test_case["name"],
                    "message": "Unknown failure",
                    "trace": traceback.format_exc()
                })
            self.increment_fail_count()
        else:
            self.append_passed_test(test_case["name"])
            self.increment_success_count()

    def print_results(self):
        """
        Basic formatting is done and the results are printed to the screen.
        """
        print("Number of Successes: {}".format(self.__successCount))
        for case in self.__passedTests:
            print("\t{}".format(case))
        print("")
        print("Number of Failures:  {}".format(self.__failCount))
        for case in self.__failedTests:
            print("****************************************")
            print(case['case'], "\n****************************************")
            print(case['trace'])
            print(case['message'])
            print("****************************************")

    def increment_success_count(self):
        """Increments the count of successes"""
        self.__successCount += 1

    def increment_fail_count(self):
        """Increments the count of failures"""
        self.__failCount += 1

    def append_passed_test(self, test):
        """Adds a result to the list of successes"""
        self.__passedTests.append(test)

    def append_failed_test(self, test):
        """Adds a result to the list of failures"""
        self.__failedTests.append(test)


if __name__ == "__main__":
    testlist = [{"module": "test.assert_test", "class": "AssertTest"}]
    otter = Otter(testlist)
    otter.run()

