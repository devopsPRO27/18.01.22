file=open(r'C:\Users\hothaifa\Desktop\test\file1.txt') # for readonly

print(file.readline()[:-1])
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
print('hii from \'PYcharm\' ')
#print(file.readlines())
print(file.read())

s=file.read() #='hii my name is hod \ni love coffe and to read antechrstos\ni love python\ni have a black seat leon '
print('hii my name is hod \ni love coffe and toread antechrstos\ni love python\ni have a black seat leon')
print(file.tell())
print(file.readline()[:-1])
file.seek(10)
print(file.tell())
print(file.readline()[:-1])
file.seek(67)
print(file.tell())
print(file.readline()[:-1])
file.seek(0)
print(file.tell())
print(file.readline()[:-1])
file.seek(0)
print(file.tell())

x=4
print('x=',x)
file.seek(0)
print(file.tell())
print(file.readline())
print(file.readlines())
for line in file.readlines():
    print(line)

for line in file.readlines():
    print(line)
file.close()