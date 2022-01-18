def isPrimeNumber(num):
    flag = False
    if num > 1:
        for i in range(2,num):
            if(num % i) == 0:
                flag = True
                break
    elif num==1:
        print(num, "is a prime number")
    else:
        print(num, "is neither a prime nor not prime number")
        return

    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

def isPrimeNumberIterative(num):
    if num >1:
        for i in range(2,num):
            if(num % i )==0:
                print(num,"is not a prime number")
                break
        else:
            print(num, "is a prime number")
    elif num==1:
        print(num, "is a prime number")
    else:
        print(num, "is neither a prime nor a not prime number")