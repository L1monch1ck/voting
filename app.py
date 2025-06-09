# 1)
def print_multiplication_table(number):
    """
    Prints the multiplication table for the given number from 1 to 10.
    """
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

print_multiplication_table(9)




# def mul(num):
#     """
#     Prints the multipliaction table of a given number
#     """
#     for i in range(1, 11):
#         print("{multiplier} * {multiplicand} = {multiplicantion}".format(
#             multiplier=num, multiplicand=i, multiplicantion=num * i))

# mul(9)



# 2)
import math

def is_prime(n):
    """
    Returns True if the given number is a prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """
    Prints all twin prime pairs up to the given limit.
    """
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            print(f"{num} and {num + 2}")

print("Twin Primes up to 1000:")
find_twin_primes(100)



# def checkPrime(max_num):
#     """
#     Check whether the given number is prime or not
#     """
#     for num in range (2, max_num):
#         if max_num % num == 0:
#             return False
#     return True

# def twinPrime(max_num):
#     """
#     Generates the list of twin primes
#     """
#     for first_num in range(2, max_num):
#         second_num = first_num + 2
#         if (checkPrime(first_num) and checkPrime(second_num)):
#             print(" {0} and {1}".format(first_num, second_num))

# print("Twin Prime: ")
# twinPrime(1000)



# 3)
import math

def prime_factors(num):
    """
    Returns the list of prime factors of a number.
    """
    factors = []

    # Делим на 2, пока делится
    while num % 2 == 0:
        factors.append(2)
        num //= 2  # целочисленное деление

    # Проверяем нечетные делители до sqrt(num)
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i

    # Если осталось простое число > 2
    if num > 2:
        factors.append(num)

    return factors

# Пример вызова
print(prime_factors(88))  # Выведет: [2, 2, 2, 7]

# import math

# prime_list = []

# def primeFactors(num):
#     """
#     Returns the prime factors of a number
#     """
    
#     # for and while loop takes care of composite numbers
#     while num % 2 == 0:
#         prime_list.append(2)
#         num = num/2
        
#     # num will be odd by now, thus complexity can be reduced by discarding even numbers
#     # sqrt is used to discard composite numbers
#     for i in range(3, int(math.sqrt(num))+1, 2):
#         while num%i == 0:
#             prime_list.append(i)
#             num = num/i

#     # when num is prime
#     if num > 2:
#         num = int(num)
#         prime_list.append(num)
#     return prime_list
        
# primeFactors(56)


# 4)

