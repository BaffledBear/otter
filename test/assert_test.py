from src.asserts import *
from src.unittest import UnitTest, TestCase


# TODO create list of classes to run that is passed to otter.run()
class AssertTest(UnitTest):

    def set_up(self):
        self.test_func = lambda x, y: x / y
        self.test_func2 = lambda x, y: x * y
        self.tObject = object()
        self.tObject2 = object()

    def tear_down(self):
        self.test_func = None
        self.test_func2 = None
        self.tObject = None
        self.tObject2 = None

    @TestCase
    def test_assert_true(self):
        assert_true(
            assert_true(True),
            message="Excepted True and got False."
        )

    @TestCase
    def test_assert_true_fail(self):
        assert_raises(
            OtterAssertError,
            assert_true,
            False,
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_equal_int(self):
        assert_true(
            assert_equal(1, 1),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_equal_str(self):
        assert_true(
            assert_equal("True", "True"),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_equal_fail_int(self):
        assert_raises(
            OtterAssertError,
            assert_equal,
            1,
            2,
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_equal_fail_str(self):
        assert_raises(
            OtterAssertError,
            assert_equal,
            "False",
            "Some Random Value",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_not_equal_int(self):
        assert_true(
            assert_not_equal(1, 2),
            message="Expected inequalilty and got equality"
        )

    @TestCase
    def test_assert_not_equal_str(self):
        assert_true(
            assert_not_equal("True", "Some random Value"),
            message="Expected equal and got inequality"
        )

    @TestCase
    def test_assert_not_equal_fail_int(self):
        assert_raises(
            OtterAssertError,
            assert_not_equal,
            1,
            1,
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_not_equal_fail_str(self):
        assert_raises(
            OtterAssertError,
            assert_not_equal,
            "False",
            "False",
            message="Expected exception and got none"
        )

    @TestCase
    def test_assert_false(self):
        assert_true(
            assert_false(False),
            message="Excepted False and got True."
        )

    @TestCase
    def test_assert_false_fail(self):
        assert_raises(
            OtterAssertError,
            assert_false,
            True,
            message="Expected False and got True."
        )

    @TestCase
    def test_assert_in_list(self):
        assert_true(
            assert_in("a", ["a", "b", "c"]),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_dict_list(self):
        assert_true(
            assert_in({"a": "b"}, [{"a": "b"}, {"c": "d"}]),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_key_in_dict(self):
        assert_true(
            assert_in("a", {"a": "b"}),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_in_fail_list(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            "e",
            ["a", "b", "c"],
            message="Expected exception and got none")

    @TestCase
    def test_assert_in_fail_dict_list(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            {"c": "b"},
            [{"a": "b"}, {"c": "d"}],
            message="Expected exception and got none")

    @TestCase
    def test_assert_in_fail_key_in_dict(self):
        assert_raises(
            OtterAssertError,
            assert_in,
            "b",
            {"a": "b"},
            message="Expected exception and got none")

    @TestCase
    def test_assert_not_in_list(self):
        assert_true(
            assert_not_in("e", ["a", "b", "c"]),
            message="Expected False and got True"
        )

    @TestCase
    def test_assert_not_in_dict_list(self):
        assert_true(
            assert_not_in({"c": "b"}, [{"a": "b"}, {"c": "d"}]),
            message="Expected False and got True"
        )

    @TestCase
    def test_assert_not_in_key_in_dict(self):
        assert_true(
            assert_not_in("b", {"a": "b"}),
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
            message="Expected exception and got none"
            )

    @TestCase
    def test_assert_not_in_fail_key_in_dict(self):
        assert_raises(
            OtterAssertError,
            assert_not_in,
            "a",
            {"a": "b"},
            message="Expected exception and got none"
            )

    @TestCase
    def test_assert_is_object(self):
        assert_true(
            assert_is(self.tObject, self.tObject),
            message="Expected True and got False"
        )

    @TestCase
    def test_assert_is_fail_object(self):
        assert_raises(
            OtterAssertError,
            assert_is,
            self.tObject,
            self.tObject2,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_func(self):
        assert_true(
            assert_is(self.test_func, self.test_func),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is,
            self.test_func,
            self.test_func2,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_object(self):
        assert_true(
            assert_is_not(self.tObject, self.tObject2),
            message="Expected True and got False.")

    @TestCase
    def test_assert_is_not_fail_object(self):
        assert_raises(
            OtterAssertError,
            assert_is_not,
            self.tObject,
            self.tObject,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_func(self):
        assert_true(
            assert_is_not(self.test_func, self.test_func2),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_not_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is_not,
            self.test_func,
            self.test_func,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_none(self):
        assert_true(
            assert_is_none(None),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_none_fail_func(self):
        assert_raises(
            OtterAssertError,
            assert_is_none,
            self.test_func,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_is_not_none_func(self):
        assert_true(
            assert_is_not_none(self.test_func),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_is_not_none_fail(self):
        assert_raises(
            OtterAssertError,
            assert_is_not_none,
            None,
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_raises(self):
        assert_true(
            assert_raises(ZeroDivisionError, self.test_func, 1, 0),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_raises_fail(self):
        assert_raises(
            OtterAssertError,
            assert_raises,
            ZeroDivisionError,
            self.test_func,
            1,
            1,
            message="Expected failure"
        )

    @TestCase
    def test_assert_type_in(self):
        assert_true(
            assert_type_in(object, [0, 5, object(), "I'm a string."]),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_type_in_false(self):
        assert_raises(
            OtterAssertError,
            assert_type_in,
            UnitTest,
            [0, 5, "I'm a string"],
            message="Expected exception and got none."
        )

    @TestCase
    def test_assert_type_not_in(self):
        assert_true(
            assert_type_not_in(UnitTest, [0, 5, object(), "I'm a string."]),
            message="Expected True and got False."
        )

    @TestCase
    def test_assert_type_not_in_false(self):
        assert_raises(
            OtterAssertError,
            assert_type_not_in,
            object,
            [0, 5, object(), "I'm a string"],
            message="Expected exception and got none."
        )
