# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.i = 2

    def __next__(self):
        for n in range(self.i, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.i = n + 1
                return n
        else:
            raise StopIteration()

    def __iter__(self):
        return self


class PrimeGeneratorIter:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return PrimeGenerator(self.stop)


print(list(PrimeGenerator(150)))
