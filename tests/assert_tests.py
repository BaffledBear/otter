from otter import Otter, make_test_list
from src.asserts import assert_true


test = make_test_list(Otter([]))

# TODO create list of classes to run that is passed to otter.run()
class AssertTest:

    def __init__(self):
        self.otter = Otter(test)
        self.otter.run()

    @test
    def test_assert_true(self):
        assert_true(
                    True,
                    "Excepted True and got False."
                    )


if __name__ == "__main__":
    cases = AssertTest()
    test = make_test_list(cases.otter)
