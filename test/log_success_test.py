from src.asserts import assert_true
from src.otter import Otter
from src.unittest import UnitTest, TestCase
from test.test_classes import test_class


class LogSuccessTest(UnitTest):
    def set_up(self):
        self.otter = Otter([])
        self.test_object = test_class()
        self.otter.set_test_list(
            [self.test_object]

        )
        self.otter.log_success({"Success Test": "Success Test"})

    def tear_down(self):
        self.otter = None

    @TestCase
    def test_success_count(self):
        assert_true(self.otter.get_success_count() == 1)

    @TestCase
    def test_success_result(self):
        assert_true(
            self.otter.get_results()[0] == {"Success Test": "Success Test"},
            message="Expected True and got False."
        )

    @TestCase
    def test_result_length(self):
        assert_true(
            len(self.otter.get_results()) == 1,
            message="Expected True and got False."
        )
