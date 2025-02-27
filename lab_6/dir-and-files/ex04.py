import os

path = r'C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_6/dir-and-files/ex04.txt'

with open(path, 'r') as f:
    lines = f.readlines()
    print('Number of lines in {}: {}'.format(os.path.basename(path), len(lines)))