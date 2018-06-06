def assert_string(x):
    """Displays an assertion error if the parameter is negative."""
    assert(x >= 0), str(x) + ' is negative!!'


def add_nums(x):
    """Adds the parameter to 2."""
    try:
        total = x + 2
    except TypeError:
        return 'parameter is not an int'
    else:
        return total


def check_zero_divisible(x, y):
    """Checks if y is not zero and if x is divisible by y."""
    try:
        total = x / y
    except:
        return str(x) + ' is not divisible by ' + str(y)
    else:
        return total


def check_tuple(x):
    """Checks if parameter is a tuple."""
    try:
        x.append('yeah')
        x[0] = 1
    except(TypeError, AttributeError):
        return str(x) + ' is a tuple'
    else:
        return str(x) + ' is not a tuple'


def check_add_by_two(x):
    """Checks if parameter can be added by 2."""
    total = 'an error'
    try:
        total = x + 2
    finally:
        return total


def check_has_append(x):
    """Checks if parameter has an append method."""
    try:
        x.append('yeah')
    except AttributeError, e:
        return 'Attribute Error: ' + str(e)
    else:
        return 'the parameter has an append method'


def raise_error():
    """Raises an error."""
    try:
        raise ImportError('import error raised')
    except ImportError, e:
        print(e)


class MyError(EOFError):

    def __init__(self, a):
        """initializes MyError class"""
        self.args = a


print(add_nums('a'))
print(check_zero_divisible(3, 0))
print(check_zero_divisible(6, 3))
print(check_tuple((1, 2, 3)))
print(check_tuple([1, 2, 3]))
print(check_add_by_two('a'))
print(check_has_append('a'))
print(check_has_append(['a', 'b', 'c']))
raise_error()
try:
    raise MyError('this is my customized EOFerror')
except MyError, e:
    total = ''
    for x in e:
        total += x
    print(total)
assert_string(-1)
