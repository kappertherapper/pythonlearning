list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiplyer = 0

for k in range(10):
    multiplyer += 1
    for i in list:
        print(i * multiplyer, end=" ")
    print()