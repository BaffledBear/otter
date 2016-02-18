# OTTER - *O*bjective *T*esting *T*oolkit for *E*arly *R*eveal
**OTTER** is a unit test framework and a work in progress

*Full Disclosure* I just really wanted to name something OTTER.

## Usage
A TestCase is a single method that tests one unit of work. A test case is defined as follows.
```python
...
@TestCase
def test_some_behavior(self):
    pass
...

A TestSuite is a collection of test cases that include similar set up and tear down steps. A TestSuite is defined as follows.
```python
...
class SuiteName(TestSuite):

    def set_up(self):
        pass

    def tear_down(self):
        pass

    @TestCase
    def test_some_behavior(self):
        pass

    @TestCase
    def test_another_behavior(self):
...

Any method in a TestSuite object will be run automatically. The set_up method will be run prior to the TestCases of each TestSuite and the tear_down will be run at the end of each TestSuite.

## Asserts & Fails
Otter includes the following assert methods that can be used by importing them from the src.asserts module. The assert methods will raise the OtterAssertError if the condition of the assert is not met.

* ```assert_true(actual)``` - Checks for the boolean value of actual.
* ```assert_false(actual)``` - Checks for the boolean value of actual.
* ```assert_equal(expected, actual)``` - Checks if expected and actual are equal.
* ```assert_not_equal(expected, actual)``` - Checks that expected and actual are not equal.
* ```assert_in(expected, collection)``` - Checks that expected is in the provided collection.
* ```assert_not_in(expected, collection)``` - Checks that expected is not in the provided collection.
* ```assert_is(expected, actual, message)``` - Checks that expected and actual are the same object.
* ```assert_is_not(expected, actual, message)``` - Checks that expected and actual are different objects.
* ```assert_is_none(actual)``` - Checks that actual is equal to None.
* ```assert_is_not_none(actual)``` - Checks that actual is not None.
* ```assert_raises(exc, func, *args)``` - Checks that the exception raised by a certain group of args for the provided function matches the exception in exc.

For each assert method there is an option message value that can be included at the end. The default is set to None and no message will be displayed in the case of a success. In certain circumstances a default error message is included and will overwrite any provided messages. These cases are when the @TestCase.expected_failure decorator is used, and when an exception other than OtterAssertError was raised.

In instances where a test case is known to fail for any reason, the @TestCase.expected_failure decorator can be used as follows.

```python
...
@TestCase
@TestCase.expected_failure
def test_case_will_fail(self):
    return 1 / 0
...

This will log the case as a failure and will set the message to "Expected Failure. This should be fixed." This decorator is used to mark cases that are known to fail to avoid confusion when testing while they are unresolved. Negative testing should use the assert_raises method in combination with another assert method as needed.
