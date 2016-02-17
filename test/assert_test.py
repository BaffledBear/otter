from src.testsuite import TestSuite, TestCase
from src.asserts import *


# TODO create list of classes to run that is passed to otter.run()
class AssertTest(TestSuite):

    def set_up(self):
        def test_func(a, b):
            return a / b

        def test_func2():
            pass

        print("success")
        self.test_func = test_func
        self.test_func2 = test_func2
        self.tObject = object()
        self.tObject2 = object()

    @TestCase
    def test_assert_true(self):
        assert_true(
            assert_true(
                True,
                message="Excepted True and got False."
            ),
            message="Excepted True and got False."
        )

    @TestCase
    def test_assert_true_fail(self):
        assert_raises(
            OtterAssertError,
            assert_true,
            False,
            "Expected False and got False.",
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_equal_int(self):
        assert_true(
            assert_equal(
                         1,
                         1,
                         "Expected equal and got inequality"
                         ),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_equal_str(self):
        assert_true(
            assert_equal(
                         "True",
                         "True",
                         "Expected equal and got inequality"
                         ),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_equal_fail_int(self):
        assert_raises(
            OtterAssertError,
            assert_equal,
            1,
            2,
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_equal_fail_str(self):
        assert_raises(
            OtterAssertError,
            assert_equal,
            "False",
            "Some Random Value",
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_not_equal_int(self):
        assert_true(
            assert_not_equal(
                             1,
                             2,
                             "Expected equal and got inequality"
                             ),
            message="Expected inequalilty and got equality"
        )

    @TestCase
    def test_assert_not_equal_str(self):
        assert_true(
            assert_not_equal(
                             "True",
                             "Some random Value",
                             "Expected inequality and got equality"
                             ),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_not_equal_fail_int(self):
        assert_raises(
            OtterAssertError,
            assert_not_equal,
            1,
            1,
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_not_equal_fail_str(self):
        assert_raises(
            OtterAssertError,
            assert_not_equal,
            "False",
            "False",
            "Expected exception and got none",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_false(self):
        assert_true(
            assert_false(
                         False,
                         "Excepted False and got True."
                         ),
            message="Excepted False and got True."
        )

    @TestCase
    def test_assert_false_fail(self):
        assert_raises(
            OtterAssertError,
            assert_false,
            True,
            "Expected False and got False.",
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_in_list(self):
        assert_true(
            assert_in(
                      "a",
                      ["a", "b", "c"],
                      "Expected Success"
                      ),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_dict_list(self):
        assert_true(
            assert_in(
                      {"a": "b"},
                      [{"a": "b"}, {"c": "d"}],
                      "Test"
                      ),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_key_in_dict(self):
        assert_true(
            assert_in(
                      "a",
                      {"a": "b"},
                      "Test"
                      ),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_fail_list(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            "e",
            ["a", "b", "c"],
            "Expected Failure",
            message="Expected exception and got none")

    @TestCase
    def test_assert_in_fail_dict_list(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            {"c": "b"},
            [{"a": "b"}, {"c": "d"}],
            "Expected Failure",
            message="Expected exception and got none")

    @TestCase
    def test_assert_in_fail_key_in_dict(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            "b",
            {"a": "b"},
            "Expected Failure",
            message="Expected exception and got none")

    @TestCase
    def test_assert_not_in_list(self):
        assert_true(
            assert_not_in(
                          "e",
                          ["a", "b", "c"],
                          "Expected Failure"
                          ),
            message="Expected False and got True"
        )

    @TestCase
    def test_assert_not_in_dict_list(self):
        assert_true(
            assert_not_in(
                          {"c": "b"},
                          [{"a": "b"}, {"c": "d"}],
                          "Test"
                          ),
            message="Expected False and got True"
        )

    @TestCase
    def test_assert_not_in_key_in_dict(self):
        assert_true(
            assert_not_in(
                          "b",
                          {"a": "b"},
                          "Test"
                          ),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_not_in_fail_list(self):
        assert_raises(
            OtterAssertError,
            assert_not_in,
            "a",
            ["a", "b", "c"],
            "Expected Failure",
            message="Expected exception and got none"
            )

    @TestCase
    def test_assert_not_in_fail_dict_list(self):
        assert_raises(
            OtterAssertError,
            assert_not_in,
            {"a": "b"},
            [{"a": "b"}, {"c": "d"}],
            "Expected Failure",
            message="Expected exception and got none"
            )

    @TestCase
    def test_assert_not_in_fail_key_in_dict(self):
        assert_raises(
            OtterAssertError,
            assert_not_in,
            "a",
            {"a": "b"},
            "Expected Failure",
            message="Expected exception and got none"
            )

    @TestCase
    def test_assert_is_object(self):
        assert_true(
            assert_is(
                self.tObject,
                self.tObject,
                message="Expected True and got False."),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_is_fail_object(self):
        assert_raises(
            OtterAssertError,
            assert_is,
            self.tObject,
            self.tObject2,
            "Expected Failure",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_func(self):
        assert_true(
            assert_is(
                self.test_func,
                self.test_func,
                message="Expected True and got False."
            ),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is,
            self.test_func,
            self.test_func2,
            "Expected  and got False.",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_object(self):
        assert_true(
            assert_is_not(
                self.tObject,
                self.tObject2,
                message="Expected True and got False."
            ),
            message="Expected True and got False.")

    @TestCase
    def test_assert_is_not_fail_object(self):
        assert_raises(
            OtterAssertError,
            assert_is_not,
            self.tObject,
            self.tObject,
            "Expected Failure",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_func(self):
        assert_true(
            assert_is_not(
                self.test_func,
                self.test_func2,
                message="Expected True and got False."
            ),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_not_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is_not,
            self.test_func,
            self.test_func,
            "Expected  and got False.",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_none(self):
        assert_true(
            assert_is_none(
                None,
                message="Expected True and got False."
            ),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_none_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is_none,
            self.test_func,
            "Expected and got False.",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_none_func(self):
        assert_true(
            assert_is_not_none(
                self.test_func,
                message="Expected True and got False."
            ),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_not_none_fail(self):
        assert_raises(
            OtterAssertError,
            assert_is_not_none,
            None,
            "Expected  and got False.",
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_raises(self):
        assert_true(
            assert_raises(
                ZeroDivisionError,
                self.test_func,
                1,
                0,
                message="Expected True and got False"),
            message="Expected True and got False."
        )

    @TestCase
    @TestCase.expected_failure
    def test_assert_raises_fail(self):
        assert_raises(
            ZeroDivisionError,
            self.test_func,
            1,
            1,
            message="Expected failure"
        )

if __name__ == "__main__":
    cases = AssertTest()
