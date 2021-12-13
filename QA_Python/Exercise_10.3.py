def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x + 1):
            if x % n == 0 and n != x:
                return False
    return True


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
notPrimes = [1, 4, 6, 8, 9, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36]
for i in primes:
    print(f"{i} - {is_prime(i)}")
print('\n\n\n')
for i in notPrimes:
    print(f"{i} - {is_prime(i)}")

