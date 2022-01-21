
err=int()
try:
    x=float(input('please enter a number'))
    y=float(input('please enter a number'))
    list1 = [x, y]
    print(x / y)
except Exception as e :
    print('============================ERROR ')
    print('something went weong ')
    print('==================================')
except ZeroDivisionError as e :
    print('============================ERROR ')
    print('you divieded by zero we cannot allow that ')
    print('==================================')
except ValueError as e:
    print(type(e))
    print('============================ERROR ')
    print('i told you to enter a number huh !!!!!!! ')
    print('==================================')
finally:
    print('try except is done')

print('end of the program')