from src.asserts import assert_true
from src.unittest import UnitTest


class test_class(UnitTest):
    """Test data to be used by RunnerTest in initialization of an Otter."""

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


class test_class_2(UnitTest):
    """Test data to be used by test cases in RunnerTest"""

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
