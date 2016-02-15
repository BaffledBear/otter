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

class OtterAssertError(Exception):
    """Raised in the event of failed assertion"""
    pass

# TODO - Update comments for docstring use
def assertTrue(actual, message):
    """Checks whether the argument is the boolean value True."""
    if actual:
        return
    else:
        raise OtterAssertError(message)


def assertEqual(expected, actual):
    """Checks for equality of the two arguments."""
    pass


def assertNotEqual(expected, actual):
    """Checks for inequality of the two arguments."""
    pass


def assertFalse(expected):
    """Checks whether the argument is the boolean value False."""
    pass


def assertIn(expected, collection):
    """Checks whether the argument is in the collection."""
    pass


def assertNotIn(expected, collection):
    """Checks whether the argument is not in the collection."""
    pass


def assertIs(expected, actual):
    """Checks whether the value is the expected."""
    pass


def assertIsNot(expected, actual):
    """Checks whether the value is not the expected."""
    pass


def assertIsNone(expected):
    """Checks whether the argument is None."""
    pass


def assertIsNotNone(expected):
    """Checks whether the argument is not None."""
    pass


def assertRaises(exception, func, *args):
    """
    Checks whether the function 'func' raises an exception of the type
    exception'.
    """
    pass
