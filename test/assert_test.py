from src.testsuite import TestSuite, TestCase
from src.asserts import *


# TODO create list of classes to run that is passed to otter.run()
class AssertTest(TestSuite):

    @TestCase
    def test_assert_true(self):
        assert_true(
            assert_true(True, "Excepted True and got False."),
            "Excepted True and got False."
        )
        assert_raises(
            OtterAssertError,
            assert_true, False, "Expected False and got False.",
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_equal(self):
        assert_true(
            assert_equal(1, 1, "Expected equal and got inequality"),
            message="Expected equal and got inequality"
        )
        assert_raises(
            OtterAssertError,
            assert_equal, 1, 2, "Expected exception and got none",
            message="Expected exception and got none"
        )
        assert_true(
            assert_equal("True", "True",
                                 "Expected equal and got inequality"),
            message="Expected equal and got inequality"
        )
        assert_raises(
            OtterAssertError,
            assert_equal, "False", "Some Random Value",
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_not_equal(self):
        assert_true(
            assert_not_equal(1, 2,
                             "Expected equal and got inequality"),
            message="Expected inequalilty and got equality"
        )
        assert_raises(
            OtterAssertError,
            assert_not_equal, 1, 1,
            "Expected exception and got none",
            message="Expected exception and got none"
        )
        assert_true(
            assert_not_equal("True", "Some random Value",
                                     "Expected inequality and got equality"),
            message="Expected equal and got inequality"
        )
        assert_raises(
            OtterAssertError,
            assert_not_equal, "False", "False",
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_false(self):
        assert_true(
            assert_false(False, "Excepted False and got True."),
            "Excepted False and got True."
        )
        assert_raises(
            OtterAssertError,
            assert_false, True, "Expected False and got False.",
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_in(self):
        assert_true(
            assert_in("a", ["a", "b", "c"], "Expected Success"),
            message="Expected True and got False"
        )
        assert_true(
            assert_in({"a": "b"}, [{"a": "b"}, {"c": "d"}], "Test"),
            message="Expected True and got False"
        )
        assert_true(
            assert_in("a", {"a": "b"}, "Test"),
            message="Expected True and got False"
        )
        assert_raises(
            OtterAssertError,
            assert_in, "e", ["a", "b", "c"], "Expected Failure",
            message="Expected exception and got none")
        assert_raises(
            OtterAssertError,
            assert_in, {"c": "b"}, [{"a": "b"}, {"c": "d"}],
            "Expected Failure",
            message="Expected exception and got none")
        assert_raises(
            OtterAssertError,
            assert_in, "b", {"a": "b"}, "Expected Failure",
            message="Expected exception and got none")

    @TestCase
    def test_assert_not_in(self):
        assert_true(
            assert_not_in("e", ["a", "b", "c"], "Expected Failure"),
            message="Expected False and got True"
        )
        assert_true(
            assert_not_in({"c": "b"}, [{"a": "b"}, {"c": "d"}],
                          "Test"),
            message="Expected False and got True"
        )
        assert_true(
            assert_not_in("b", {"a": "b"}, "Test"),
            message="Expected True and got False"
        )
        assert_raises(
            OtterAssertError,
            assert_not_in, "a", ["a", "b", "c"], "Expected Failure",
            message="Expected exception and got none")
        assert_raises(
            OtterAssertError,
            assert_not_in, {"a": "b"}, [{"a": "b"}, {"c": "d"}],
            "Expected Failure",
            message="Expected exception and got none")
        assert_raises(
            OtterAssertError,
            assert_not_in, "a", {"a": "b"}, "Expected Failure",
            message="Expected exception and got none")

if __name__ == "__main__":
    cases = AssertTest()
