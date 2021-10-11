print('Multiplication file')
import calculations.division
from . import  division


import config

csv_file_path = config.CSV_FILE_PATH

print('CSV file path is >>>>>>>> ',csv_file_path)

def mul(x,y):
    mul1 = x * y
    print(f'Multiplication of {x} and {y} is {mul1}')
    return mul1

if __name__ == "__main__":
    mul(5,6)