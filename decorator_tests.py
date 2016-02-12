from functools import wraps

# Using individual decorators and a function defined outside of a class


def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

print(get_text("John"))
print(get_text.__name__)

# Using generic @tags decorator and a method defined in Person class


def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))
        return func_wrapper
    return tags_decorator


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @tags("p")
    def get_fullname(self):
        return self.name + " " + self.family

my_person = Person()
print(my_person.get_fullname())
print(my_person.get_fullname.__name__)


# Using a registry decorator to make a list of functions
def makeTestList():
    testList = {}

    def listBuilder(func):
        testList[func.__name__] = func
        return func
    listBuilder.all = testList
    return listBuilder

test = makeTestList()


@test
def test_decorator_listing(value):
    print(value)

print(test.all)
for func in test.all:
    test.all[func]("BOOM")


# Decorate a decorator as a decorator in a registry

def makeRegisteringDecorator(foreignDecorator):
    """
        Returns a copy of foreignDecorator, which is identical in every
        way(*), except also appends a .decorator property to the callable it
        spits out.
    """
    def newDecorator(func):
        # Call to newDecorator(method)
        # Exactly like old decorator, but output keeps track of what
        # decorated it
        R = foreignDecorator(func)  # apply foreignDecorator, like call to
        # foreignDecorator(method) would have done
        R.decorator = newDecorator  # keep track of decorator
        # R.original = func         # keep track of everything
        return R

    newDecorator.__name__ = foreignDecorator.__name__
    newDecorator.__doc__ = foreignDecorator.__doc__
    return newDecorator

deco = makeRegisteringDecorator(tags('p'))


class Test2(object):
    @deco
    def method(self):
        print("Success!")

    @tags('p')
    def method2(self):
        print("Success2!")


def methodsWithDecorator(cls, decorator):
    """
        Returns all methods in CLS with DECORATOR as the
        outermost decorator.

        DECORATOR must be a "registering decorator"; one
        can make any decorator "registering" via the
        makeRegisteringDecorator function.
    """
    for maybeDecorated in cls.__dict__.values():
        if hasattr(maybeDecorated, 'decorator'):
            if maybeDecorated.decorator == decorator:
                print(maybeDecorated)
                yield maybeDecorated

print(list(methodsWithDecorator(Test2, deco)))
