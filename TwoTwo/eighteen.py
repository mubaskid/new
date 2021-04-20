a = ['hello', 9, 3.14, 9]
for item in a:
    print(item, end='')
    if item != a[-1]:
        print(', ')
