globalvar = 'unchanged'


def printfunc(x):
    "prints the passed parameter"
    print(x)


def add(x, y):
    "adds both int parameters"
    print(x + y)


def sub(x, y):
    "returns the difference of both int parameters"
    return x - y


def concat(x, y):
    "concatenates both string parameters"
    print(str(x) + str(y))


def addelement(x, y):
    "adds element y into list x"
    x.append(y)
    print(x)


def fullname(firstname, lastname):
    "returns the fullname"
    print(firstname + ' ' + lastname)


def addword(x, y='world'):
    "adds word y into word x. by default, 'world' is added"
    print(str(x) + str(y))


def addmultiple(*args):
    "returns the sum of multiple int parameters not less than 2"
    total = 0
    if(len(args) >= 2):
        for x in args:
            total += x
        return total
    return 'needed 2 parameters'


def multiply(x, y):
    "returns the product of both int parameters"
    return x * y


def nochangeglobal(x):
    "does nothing to global variable globalvar"
    globalvar = x


printfunc('hello')
add(1, 1)
print(sub(1, 1))
concat(1, 1)
addelement([1, 2, 3], 4)
fullname('Shem', 'Ipanag')
addword('hello ')
print(addmultiple(1, 2, 3, 4, 5))
print(multiply(1, 2))
nochangeglobal('change')
print(globalvar)
