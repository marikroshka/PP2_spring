import os 

path = r'C:/Users/User/Documents/PPSPRING/py/PP2_2024Spring-main/lab_6'

if os.path.exists(path):
    print('Path exists')
    print('Filename:', os.path.basename(path))
    print('Directory:', os.path.dirname(path))
else:
    print('This path doesn\'t exist')