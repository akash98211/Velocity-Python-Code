print('Hello')
print('We are testing Calculation Module')
print('Value in __name__ variable is >>> ',__name__)  # __main__

var1 = 100
d1 = {'a': 'python', 'b':'data science'}
def addition(a,b):
    c = a + b
    print(f'Addition of {a} and {b} is {c}')
    return c

def multiplication(a,b):
    mul = a * b
    print(f'Multiplication of {a} and {b} is {mul}')
    return mul



def division(a,b):
    div = a /b
    print(f'Division of {a} and {b} is {div}')
    return div

class NewClass():
    pass

if __name__ == "__main__":   #  '__main__' == "__main__" # True
    addition(10,30)
    multiplication(2,3)
    division(10,2)
