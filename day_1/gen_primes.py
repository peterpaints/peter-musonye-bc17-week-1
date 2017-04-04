def gen_primes(n):
    # From the tests, we require input n to be an int only, and a positive one.
    if not isinstance(n, int):
        raise ValueError("Only positive integers are allowed as input")
    elif n < 1:
        raise ValueError("Only integers greater than 0 are allowed")
    else:
        """Generate prime numbers from 1 up to the specified number n."""
        prime_numbers = []
        for i in xrange(1, n + 1, 2):   # xrange, and skip all even numbers.
            prime = True
            # This filters out non-primes. A prime number is not divisible
            # by any number other than itself
            for j in xrange(2, i - 1):
                if i % j == 0:
                    prime = False
            if prime:   # if prime is not false.
                prime_numbers.append(i)
        return prime_numbers

# test case n
# print
gen_primes(1000000)

import time
start_time = time.time()
# main()
print("--- %s seconds ---" % (time.time() - start_time))

# gen_primes(39) logs 0.00000214576721191 seconds
# gen_primes(10000) logs 0.00000309944152832 seconds
# gen_primes(1000000) did not finish.
