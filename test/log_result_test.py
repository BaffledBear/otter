from src.asserts import assert_true
from src.otter import Otter
from src.unittest import UnitTest, TestCase
from test.test_classes import test_class


class LogResultTest(UnitTest):
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
    def test_log_result_success(self):
        assert_true(True)

    @TestCase
    def test_log_result_fail(self):
        assert_true(True)
