def show(row, col):
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print(i * j, end=' ')
        print()


row = int(input('enter row= '))
col = int(input('enter col= '))
print('~~~~~~~~~~~~~~~~~~~')
show(row, col)