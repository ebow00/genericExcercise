"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""


def check_prime(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                # print('{} equals {} * {}.'.format(n, x, n // x))
                break
        else:
            # print('{} is a prime number.'.format(n))
            print(n)


def prime_generator(bound):
    for n in range(2, bound):
        for x in range(2, n):
            if n % x == 0:
                # print('{} equals {} * {}.'.format(n, x, n // x))
                break
        else:
            # print('{} is a prime number.'.format(n))
            yield n


pg = prime_generator(100)
print(list(pg))
