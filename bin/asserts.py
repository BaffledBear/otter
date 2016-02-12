#
# I'm setting this file up for where I'm planning to go with it.
# I took a list of assert methods from https://github.com/zillolo/vsut-python
# because that was a good start and set them up with pass statements and basic
# comments. I will be expanding on this soon. I'm also intending to expland
# on the docstrings to provide more useful information for each method and
# the class as a whole.
#

"""
asserts.py defines the assert methods and the behaviors that are used by them.
"""

# TODO - Update comments for docstring use
"""Checks whether the argument is the boolean value True."""


def assertTrue(runner, statusBool, testCase):
    if statusBool:
        runner.increment_success_count()
        runner.append_passed_test(testCase)
    else:
        runner.increment_fail_count()
        runner.append_failed_test(testCase)


"""
Checks for equality of the two arguments.
"""


def assertEqual(runner, expected, actual):
    pass

"""
Checks for inequality of the two arguments.
"""


def assertNotEqual(runner, expected, actual):
    pass

"""
Checks whether the argument is the boolean value False.
"""


def assertFalse(runner, expected):
    pass

"""
Checks whether the argument is in the collection.
"""


def assertIn(runner, expected, collection):
    pass

"""
Checks whether the argument is not in the collection.
"""


def assertNotIn(runner, expected, collection):
    pass

"""
Checks whether the value is the expected.
"""


def assertIs(runner, expected, actual):
    pass

"""
Checks whether the value is not the expected.
"""


def assertIsNot(runner, expected, actual):
    pass

"""
Checks whether the argument is None.
"""


def assertIsNone(runner, expected):
    pass

"""
Checks whether the argument is not None.
"""


def assertIsNotNone(runner, expected):
    pass

"""
Checks whether the function 'func' raises an exception of the type
exception'.
"""


def assertRaises(runner, exception, func, *args):
    pass
