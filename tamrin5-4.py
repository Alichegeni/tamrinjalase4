def factorial():
    number=int(input("Enter your desired number : "))
    m=1
    for i in range(1,number+1):
        m=m*i
        if m==number:
            print('F!',i,':',number)
            break
        if i==number and m != number :
            print("the number Not obtained from factorial")
factorial()
