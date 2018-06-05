num = 4
fnum = 1.1

num2 = 2
num2 += num
print num2

num2 -= num
print num2

num2 *= num
print num2

num2 /= num
print num2

num2 %= num
print num2

num2 **= num
print num2

num2 //= fnum
print num2

string = "Hello World"
lst=[1,2,3,"y","n"]
tpl=("y","n",1,2,3)
dct={"one":1.3,"two":2,3:"three"}

print(num + fnum)
print(fnum -num)
print(num * 2)
print(fnum % 1)
print(num/2)
print(num**2)
print(fnum//1)
print(num==fnum)
print(fnum!=num)
print(num>fnum)
print(num<fnum)
print("true" and 1)
print(0 or 1)
print(not num)
print(2 in lst)
print(4 not in tpl)
print(dct[3] is 3)
print(dct["one"] is not 1)