def assertstring(x):
    "displays an assertion error if the parameter is negative"
    assert(x >= 0), str(x) + ' is negative!!'


def addnums(x):
    "adds the parameter to 2"
    try:
        total = x + 2
    except TypeError:
        return 'parameter is not an int'
    else:
        return total


def checkzerodivisible(x, y):
    "checks if y is not zero and if x is divisible by y"
    try:
        total = x / y
    except:
        return str(x) + ' is not divisible by ' + str(y)
    else:
        return total


def checktuple(x):
    "checks if parameter is a tuple"
    try:
        x.append('yeah')
        x[0] = 1
    except(TypeError, AttributeError):
        return str(x) + ' is a tuple'
    else:
        return str(x) + ' is not a tuple'


def checkaddbytwo(x):
    "checks if parameter can be added by 2"
    total = 'an error'
    try:
        total = x + 2
    finally:
        return total


def checkhasappend(x):
    "checks if parameter has an append method"
    try:
        x.append('yeah')
    except AttributeError, e:
        return 'Attribute Error: ' + str(e)
    else:
        return 'the parameter has an append method'


def raiseerror():
    "raises an error"
    try:
        raise ImportError('import error raised')
    except ImportError, e:
        print(e)


class MyError(EOFError):
    def __init__(self, a):
        self.args = a

print(addnums('a'))
print(checkzerodivisible(3, 0))
print(checkzerodivisible(6, 3))
print(checktuple((1, 2, 3)))
print(checktuple([1, 2, 3]))
print(checkaddbytwo('a'))
print(checkhasappend('a'))
print(checkhasappend(['a', 'b', 'c']))
raiseerror()
try:
    raise MyError('this is my customized EOFerror')
except MyError, e:
    total = ''
    for x in e:
        total += x
    print(total)
# assertstring(-1)
