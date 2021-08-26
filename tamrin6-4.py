a = int(input('enter a number:'))
b = int(input('enter a number:'))

if a > b:
    a, b = b, a
    

for i in range(1, a + 1):
    if a % i == 0 and b % i == 0:
         bmm = i

print('bmm:', bmm)