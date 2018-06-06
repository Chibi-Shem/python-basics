global_var = 'unchanged'


def print_func(x):
    """Prints the passed parameter."""
    print(x)


def add(x, y):
    """Adds both int parameters."""
    print(x + y)


def sub(x, y):
    """Returns the difference of both int parameters."""
    return x - y


def concat(x, y):
    """Concatenates both string parameters."""
    print(str(x) + str(y))


def add_element(x, y):
    """Adds element y into list x."""
    x.append(y)
    print(x)


def fullname(firstname, lastname):
    """Returns the fullname."""
    print(firstname + ' ' + lastname)


def add_word(x, y='world'):
    """Adds word y into word x.  By default, 'world' is added."""
    print(str(x) + str(y))


def add_multiple(*args):
    """Returns the sum of multiple int parameters not less than 2."""
    total = 0
    if(len(args) >= 2):
        for x in args:
            total += x
        return total
    return 'needed 2 parameters'


def multiply(x, y):
    """Returns the product of both int parameters."""
    return x * y


def no_change_global(x):
    """Does nothing to global variable global_var."""
    global_var = x


print_func('hello')
add(1, 1)
print(sub(1, 1))
concat(1, 1)
add_element([1, 2, 3], 4)
fullname('Shem', 'Ipanag')
add_word('hello ')
print(add_multiple(1, 2, 3, 4, 5))
print(multiply(1, 2))
no_change_global('change')
print(global_var)
