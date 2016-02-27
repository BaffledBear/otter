from src.asserts import assert_equal, assert_is
from src.otter import Otter, Status
from src.unittest import UnitTest, TestCase
from test.test_classes import test_class


class ExecuteTestFailureTest(UnitTest):
    def set_up(self):
        self.otter = Otter([])
        self.test_object = test_class()
        self.otter.set_test_list(
            [self.test_object]
        )
        self.otter.get_test_list()[0].set_up()
        self.unit = self.otter.get_test_list()[0]
        self.case = {
            "func": test_class.test_case_two,
            "name": "test_case_two"
        }
        self.otter.execute_test(self.unit, self.case)
        self.result = self.otter.get_results()[0]

    def tear_down(self):
        self.otter = None

    @TestCase
    def test_execute_test_status(self):
        assert_equal(
            self.result["status"],
            Status.FAIL,
            message="Status was not OK."
        )

    @TestCase
    def test_execute_test_message(self):
        assert_equal(
            self.result["message"],
            "I Failed."
        )

    @TestCase
    def test_execute_test_unit(self):
        assert_is(
            self.result["unit"],
            self.unit
        )

    @TestCase
    def test_execute_test_case(self):
        assert_is(
            self.result["case"],
            self.case["name"]
        )
