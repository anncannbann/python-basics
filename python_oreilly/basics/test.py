print('hello')

#****************************
# FACTORIAL
#****************************

def factorial(num):
    product = 1
    if(num<0):
        print('Negative number, factorial doesnt exist')
    elif num==0:
        return 1
    else:
        return factorial(num-1) *num



# how to write Assertions 
def equals(actual,expected):
    assert actual == expected, f'Expected {expected}, got {actual}'



# print(equals(factorial(0),1))
# print(equals(factorial(1),1))
# print(equals(factorial(2),2))
# print(equals(factorial(4),24))
print(factorial(5))



