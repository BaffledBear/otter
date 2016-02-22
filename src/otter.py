from datetime import datetime
from enum import Enum
from importlib import import_module, reload
from src.asserts import OtterAssertError
import sys
import traceback


class Status(Enum):
    OK = 0
    FAIL = 1
    ERR = 2
    Stat = 50


class Otter(object):

    def __init__(self, unitTestList):
        """
        unitTestList should be a list of dictionaries. Key "module" should
        point to a string value of the location of a file with a UnitTest
        class. Key "class" should point to a string with the name of the class.
        """
        self.__successCount = 0
        self.__failCount = 0
        self.__results = []
        self.runStartTime = datetime.now()
        self.unitTestInstanceList = []
        for unit in unitTestList:
            self.append_test_unit_list(unit)

    def run(self):
        """
        Iterates through the instantiated list of UnitTests followed by their
        test cases and executes each case. Currently does not support arguments
        in the test cases. Setup and teardown methods are not called yet,
        either.
        """
        for unit in self.unitTestInstanceList:
            unit.set_up()
            for case in unit.get_test_list():
                self.execute_test(unit, case)
            unit.tear_down()

    def append_test_unit_list(self, unit):
        """
        Appends unit to the unitTestInstanceList.
        """
        try:
            if unit["module"] in sys.modules:
                module = reload(sys.modules[unit["module"]])
            else:
                module = import_module(unit["module"])
        except ImportError as e:
            print(e)
            return
        try:
            unitTest = getattr(module, unit["class"].rstrip())
        except Exception as e:
            print(e)
            return
        self.unitTestInstanceList.append(unitTest())

    def execute_test(self, unit, test_case):
        """
        Executes the function assigned in test_case and calls the proper log
        methods as needed. OtterAssertErrors are caught here. The flow should
        not break during any exceptions so generic exceptions are caught as and
        logged as well.
        """
        startTime = datetime.now()
        try:
            test_case["func"](unit)
        except OtterAssertError as e:
            runtime = self.get_runtime(startTime)
            if test_case["name"] in unit.expectedFailList:
                self.log_fail(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.FAIL,
                        "message": "Expected Failure. This should be fixed.",
                        "trace": e.args[0],
                        "runtime": runtime
                    }
                )
            else:
                self.log_fail(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.FAIL,
                        "message": e.args[0],
                        "trace": traceback.format_exc(),
                        "runtime": runtime
                    }
                )
        except Exception as e:
            runtime = self.get_runtime(startTime)
            if test_case["name"] in unit.expectedFailList:
                self.log_fail(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.FAIL,
                        "message": "Expected Failure. This should be fixed.",
                        "trace": traceback.format_exc(),
                        "runtime": runtime
                    }
                )
            else:
                self.log_fail(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.ERR,
                        "message": e.__class__.__name__,
                        "trace": traceback.format_exc(),
                        "runtime": runtime
                    })
        else:
            runtime = self.get_runtime(startTime)
            if test_case["name"] in unit.expectedFailList:
                self.log_fail(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.FAIL,
                        "message": "Expected this to fail and it didn't.",
                        "trace": "No traceback for successes",
                        "runtime": runtime
                    }
                )
            else:
                self.log_success(
                    {
                        "unit": unit,
                        "case": test_case["name"],
                        "status": Status.OK,
                        "message": "",
                        "runtime": runtime
                    }
                )

    def print_results(self):
        """
        Basic formatting is done and the results are printed to the screen.
        """
        self.print_table()

    def log_success(self, test):
        """Adds a result to the list of results and increments successes."""
        self.log_result(test)
        self.__successCount += 1

    def log_fail(self, test):
        """Adds a result to the list of results and increments failures."""
        self.log_result(test)
        self.__failCount += 1

    def log_result(self, test):
        """Appends the test to the list of results"""
        self.__results.append(test)

    def get_results(self):
        return self.__results

    def set_test_list(self, unitList):
        self.unitTestInstanceList = unitList

    def get_runtime(self, startTime):
        """Get the duration and return a formated as seconds"""
        delta = datetime.now() - startTime
        runtime = delta.seconds + (delta.microseconds / 1000000)
        timeStr = "{0:.{1}f}".format(runtime, 6)
        return timeStr

    def print_table(self):
        """Print the results in a table format"""
        print("\n    {0:10}  |  {1:39} | {2:4} | {3:10} | {4}".format(
            "UNIT",
            "CASE",
            "STAT",
            "TIME (SEC)",
            "MESSAGE"))
        print()
        for result in self.__results:
            print("    {0:10}  |  {1:39} | {2:4} |  {3:9} | {4}".format(
                type(result["unit"]).__name__,
                result["case"],
                result["status"].name,
                result["runtime"],
                result["message"],
            )
            )
        print(
            "\nTotal runtime: {} seconds".format(
                self.get_runtime(self.runStartTime))
        )