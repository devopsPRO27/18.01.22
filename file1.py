fileHandler=open(r'C:\Users\hothaifa\Desktop\test\file1.txt','r') #mode readonly
print(fileHandler.readline())#str
print(fileHandler.tell())
fileHandler.seek(0)
print(fileHandler.readlines()) # list
print(fileHandler.tell())
fileHandler.seek(0)
print(fileHandler.read()) # str
for line in fileHandler:
    print(line,end="")
fileHandler.close()

with open(path,'r') as file: #we dont need to close the file handler after the red
    for line in file:
        print(line[:-1])
        for lit in line[:-1]:
            print(lit)
with open(path,'w') as file:
    #print(file)
    #print(file.tell())
    for x in range(100):
        file.write(f'{x}\n')
with open(path,'r') as file:
    print(int(file.readlines()[6][:-1]))   #'6\n'[:-1] > int('6')> 6

with open(path,'w+') as file1:
    for x in range(0,300):
        file1.write(f'{x}\n')
    print(file1.tell())
    file1.seek(150)
    print(file1.readlines())
    print(file.readlines()[:file.tell//2])

with open(path,'r+') as fiileHandler:
    fiileHandler.seek(0,2)# -- move to the end of the file
    ls=fiileHandler.read()
    fiileHandler.seek(0)
    fiileHandler.write('bla bla')
    fiileHandler.write(ls)


with open(r'C:\Users\hothaifa\Desktop\test\file1.txt','r') as file1:

    with open(r'C:\Users\hothaifa\Desktop\test\file2.txt','w') as file2:
        for line in file1:
            if line.count(' ')>0:
                file2.write(line)

