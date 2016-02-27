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
def assert_true(actual, message=None):
    """
    Checks whether the argument is the boolean value True. Raises
    OtterAssertError if actual is false.
    """
    if actual:
        return True
    else:
        raise OtterAssertError(message)


def assert_false(actual, message=None):
    """
    Checks whether the argument is the boolean value False. Raises
    OtterAssertError if actual is True"""
    if actual:
        raise OtterAssertError(message)
    else:
        return True


def assert_equal(expected, actual, message=None):
    """
    Checks for equality of the two arguments. Raises OtterAssertError if
    the two arguments are not equal.
    """
    if expected == actual:
        return True
    else:
        raise OtterAssertError(message)


def assert_not_equal(expected, actual, message=None):
    """
    Checks for inequality of the two arguments. Raises OtterAssertError if
    the two arguments are equal.
    """
    if not expected == actual:
        return True
    else:
        raise OtterAssertError(message)


def assert_in(expected, collection, message=None):
    """
    Checks whether the argument is in the collection. Raises
    OtterAssertError if expected is not in the collection.
    """
    if expected in collection:
        return True
    else:
        raise OtterAssertError(message)


def assert_not_in(expected, collection, message=None):
    """
    Checks whether the argument is not in the collection. Raises
    OtterAssertError if expected is in the collection.
    """
    if expected in collection:
        raise OtterAssertError(message)
    else:
        return True


def assert_type_in(expected, collection, message=None):
    """
    Checks whether the expected type is a collection of objects. Raises
    OtterAssertError if expected is not present in the collection.
    """
    for obj in collection:
        if isinstance(obj, expected):
            return True
    raise OtterAssertError(message)


def assert_type_not_in(expected, collection, message=None):
    """
    Checks whether the expected type is not in the collection of objects.
    Raises OtterAssertError if expected is in the collection.
    """
    for obj in collection:
        if type(obj) == expected:
            raise OtterAssertError(message)
    return True


def assert_is(expected, actual, message=None):
    """
    Checks whether the value is the expected. Raises
    OtterAssertError if expected points to a different object than actual.
    """
    if expected is actual:
        return True
    else:
        raise OtterAssertError(message)


def assert_is_not(expected, actual, message=None):
    """
    Checks whether the value is not the expected. Raises
    OtterAssertError if expected points to the same object as actual.
    """
    if expected is actual:
        raise OtterAssertError(message)
    else:
        return True


def assert_is_none(actual, message=None):
    """
    Checks whether the argument is None. Raises
    OtterAssertError if actual has a value.
    """
    if actual is None:
        return True
    else:
        raise OtterAssertError(message)


def assert_is_not_none(actual, message=None):
    """
    Checks whether the argument is not None. Raises
    OtterAssertError if actual is None.
    """
    if actual is None:
        raise OtterAssertError(message)
    else:
        return True


def assert_raises(exc, func, *args, message=None):
    """
    Checks whether the function 'func' raises an exception of the type
    exception'. Raises OtterAssertError if the expected exception is not raised
    when executing the function with the provided arguments.
    """
    try:
        func(*args)
    except exc:
        return True
    else:
        raise OtterAssertError(message)
