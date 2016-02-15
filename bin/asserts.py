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


def log_results(runner, result, testCase):
    """
    Logs the results of an assert.
    """
    if result:
        runner.increment_success_count()
        runner.append_passed_test(testCase)
    else:
        runner.increment_fail_count()
        runner.append_failed_test(testCase)


# TODO - Update comments for docstring use
def assertTrue(runner, statusBool, testCase):
    """Checks whether the argument is the boolean value True."""
    log_results(runner, statusBool, testCase)


def assertEqual(runner, expected, actual):
    """Checks for equality of the two arguments."""
    pass


def assertNotEqual(runner, expected, actual):
    """Checks for inequality of the two arguments."""
    pass


def assertFalse(runner, expected):
    """Checks whether the argument is the boolean value False."""
    pass


def assertIn(runner, expected, collection):
    """Checks whether the argument is in the collection."""
    pass


def assertNotIn(runner, expected, collection):
    """Checks whether the argument is not in the collection."""
    pass


def assertIs(runner, expected, actual):
    """Checks whether the value is the expected."""
    pass


def assertIsNot(runner, expected, actual):
    """Checks whether the value is not the expected."""
    pass


def assertIsNone(runner, expected):
    """Checks whether the argument is None."""
    pass


def assertIsNotNone(runner, expected):
    """Checks whether the argument is not None."""
    pass


def assertRaises(runner, exception, func, *args):
    """
    Checks whether the function 'func' raises an exception of the type
    exception'.
    """
    pass
