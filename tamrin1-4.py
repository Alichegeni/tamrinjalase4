def show(row, col):

    for i in range(row):
        for j in range(col):
            if (i + j) % 2 == 0:
                print('#', end='')

            else:
                print('*', end='')

        print()



row = int(input('enter row= '))
col = int(input('enter col= '))

print('~~~~~~~~~~~~~~~~~~~~')

show(row, col)