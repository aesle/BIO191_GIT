def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def first_n_primes(n):
    count = 0
    num = 2
    while count < n:
        if prime(num):
            print(num, end=" ")
            count += 1
        num += 1

n = int(input("Enter the value of n: "))
first_n_primes(n)
