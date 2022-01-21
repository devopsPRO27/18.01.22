#files
'''file=open(r'D:\hothaifa\file1.txt','r+') #readonly  file2=open(r'D:\hothaifa\file1.txt')

#print(file.read())
#print(file.readline()[:-1])
#print(file.readline(),end='')
#print(file.readline())
#print(file.readlines()[1])
#print('hiiiiiiiiiiiiiiiiiiiii')
#for line in file:
#    if '\n' in line:
#        print(line,end='')
print(file.tell())
print(file.readlines())
print(file.tell())
file.write('i love my life')
print(file.tell())

file.close()'''

with open(r'D:\hothaifa\file1.txt') as fileHandler:
    with open() as fileHandler2:
    print(fileHandler.read())
print('after the with ')



