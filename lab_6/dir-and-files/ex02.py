import os 

path = 'C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_6'

print('Exists:', os.access(path, os.F_OK))
print('Access to read:', os.access(path, os.R_OK))
print('Access to write:', os.access(path, os.W_OK))
print('Can be executed:', os.access(path, os.X_OK))