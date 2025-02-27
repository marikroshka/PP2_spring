with open('dir-and-files/ex04.txt', 'r') as f1:
    with open('dir-and-files/ex07.txt', 'w') as f2:
        f2.write(f1.read())