#
# The change of the unittestframework class to the otterassert class
# happened in GitHub. I haven't updated this file to make that association yet.
# My test runner is very basic at this point because my intent is to set up
# @test decorator that will be used to determine test cases and all I wanted
# to do at this point was verify the asserTrue() call worked properly.
# In addition, I will be breaking up some of the otterassert features
# and adding them to this file.
#

import sys, traceback
from asserts import assertTrue, OtterAssertError
from functools import wraps


class Otter:

    __successCount = 0
    __failCount = 0
    __passedTests = []
    __failedTests = []
    testCases = []

    def __init__(self, testCases):
        self.testCases = testCases

    def run(self):
        for case in self.testCases.all:
            self.execute_test(self.testCases.all[case])
        self.print_results()

    def execute_test(self, test_case):
        try:
            test_case()
        except:
            print("Got an exception!", sys.exc_info()[0])
            print("In test case: ", test_case.__name__)
        #else:
            

    def print_results(self):
        print("Number of Successes: {}".format(self.__successCount))
        for case in self.__passedTests:
            print("\t{}".format(case))
        print("")
        print("Number of Failures:  {}".format(self.__failCount))
        for case in self.__failedTests:
            print("\t{}".format(case))

    def get_success_count(self):
        return self.__successCount__

    def get_fail_count(self):
        return self.__failCount__

    def increment_success_count(self):
        self.__successCount += 1

    def increment_fail_count(self):
        self.__failCount += 1

    def append_passed_test(self, test):
        self.__passedTests.append(test)

    def append_failed_test(self, test):
        self.__failedTests.append(test)


def make_test_list():
    """
    make_test_list will pick up any @test decorators and add the function to a.
    list. The list is then used as part of the Otter object instantiation to
    give a list of test cases to be run.
    """
    testList = {}

    def list_builder(func):
        @wraps(func)
        def wrapper_func(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except OtterAssertError as e:
                otter.append_failed_test(e.args[0])
                otter.increment_fail_count()
            except:
                otter.append_failed_test(func.__name__)
                otter.increment_fail_count()
            else:
                otter.append_passed_test(func.__name__)
                otter.increment_success_count()
        testList[func.__name__] = wrapper_func
        return wrapper_func
    list_builder.all = testList
    return list_builder

test = make_test_list()


@test
def case_1():
    assertTrue(True, "Case 1")


@test
def case_2():
    assertTrue(False, "Case 2")


@test
def case_3():
    assertTrue(True, "Case 3")


otter = Otter(test)
otter.run()