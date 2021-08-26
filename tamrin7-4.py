a = int(input('enter a number:'))
b = int(input('enter a number:'))

if a > b:
    c = a
    a = b
    b = c 

for i in range(b, a * b + 1):
    if i % a == 0 and i % b == 0:
        kmm = i
        break
print('kmm:', kmm)