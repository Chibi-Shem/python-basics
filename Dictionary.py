dct = {'a': 1, 'b': 2, 3: 'three'}
print(dct)
print(dct['a'])
print(dct[3])
dct[3] = 'tree'
print(dct[3])
del dct[3]
print(dct)
x = 'X'
dct2 = {'x': x, 'y': 8, 'z': 9}
print(dct2)
print(str(dct) + 'this string')
print(type(dct))
dct.clear()
dct = dct.fromkeys((1, 2, 3), 'oh')
dct[3] = 'last index'
print(dct.get(3))
print(0 in dct)
print(dct.items()[0])
print(dct.keys(), dct.values())
dct.update(dct2)
print(dct)
dct.update({'new': 100})
print(dct)
