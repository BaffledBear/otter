from src.asserts import assert_true
from src.otter import Otter
from src.unittest import UnitTest, TestCase


class test_class(UnitTest):
    def set_up(self):
        self.testList = [
                {
                    "name": "test_case_one",
                    "func": self.test_case_one
                },
                {
                    "name": "test_case_two",
                    "func": self.test_case_two
                }
            ]

    def test_case_one(self):
        assert_true(True, "I Passed.")

    def test_case_two(self):
        assert_true(False, "I Failed.")

    def tear_down(self):
        pass


class RunnerTest(UnitTest):

    def set_up(self):
        self.otter = Otter([])
        self.test_object = test_class()
        self.otter.set_test_list(
            [self.test_object]

        )
        self.otter.run()

    def tear_down(self):
        self.otter = None

    @TestCase
    def test_append_test_unit_list(self):
        pass

    @TestCase
    def test_execute_test(self):
        pass

    @TestCase
    def test_log_success(self):
        pass

    @TestCase
    def test_log_result(self):
        pass
