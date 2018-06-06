import os

print('hello python')
x = raw_input('input something: ')
print('you typed: ' + x)
x = input('input an expression: ')
print('the answer is: ' + str(x))
myfile = open('testfile', 'a')
print(myfile.name)
print(myfile.mode)
print(myfile.closed)
myfile.write('!!!\n')
myfile.close()
myfile = open('testfile', 'r')
for word in myfile.readlines():
    print(word)
myfile.seek(0, 0)
print(myfile.read(10))
print(myfile.tell())
myfile.close()

print(os.getcwd())
