import time, timeit


class CodeTimer:

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"\nFunction runtime = {self.end - self.start} sec.")


def power(limit):
    return [x**2 for x in range(limit)]


# start = time.time()
# end = time.time()
with CodeTimer() as timer:
    power(10000000)


print(timeit.timeit("[x**2 for x in range(100)]"))
