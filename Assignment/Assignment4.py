def prime_number(num):
    if num>1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not prime number")


prime_number(7)