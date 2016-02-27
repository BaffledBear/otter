from src.asserts import assert_type_in
from src.otter import Otter
from src.unittest import UnitTest, TestCase
from test.test_classes import test_class, test_class_2


class AppendUnitTest(UnitTest):

    def set_up(self):
        self.otter = Otter([])
        self.test_object = test_class()
        self.otter.set_test_list(
            [self.test_object]
        )
        self.otter.run()
        self.otter.append_test_unit_list({
                                         "class": "test_class_2",
                                         "module": "test.append_unit_test"
                                         })

    def tear_down(self):
        self.otter = None

    @TestCase
    def test_append_test_unit_list(self):
        assert_type_in(
            test_class_2,
            self.otter.unitTestInstanceList,
            message="Expected class, test_class_2, not present."
        )
