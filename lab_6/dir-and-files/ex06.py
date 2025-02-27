import os

path = r'C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_6/dir-and-files/ex06_A-Z_files'

if not os.path.exists(path):
   os.makedirs(path)

A = ord('A')
base = 'C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_6/dir-and-files/ex06_A-Z_files\\{}.txt'
for i in range(A, A+26):
    f = open(base.format(chr(i)), 'w')