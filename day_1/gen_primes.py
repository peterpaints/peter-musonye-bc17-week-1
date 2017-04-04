def gen_primes(n):
    # From the tests, we require input n to be an int only, and a positive one.
    if not isinstance(n, int):
        raise ValueError("Only positive integers are allowed as input")
    elif n < 1:
        raise ValueError("Only integers greater than 0 are allowed")
    else:
        """Generate prime numbers from 1 up to the specified number n."""
        # Modified this function to implement a sieve of erastothenes.
        prime_numbers = [2] # let's have 2 here, so that we can skip all even numbers in the outer loop
        sieve = [True] * (n + 1)
        for i in xrange(3, n + 1, 2):   # xrange, and skip all even numbers.
            if sieve[i]:
                prime_numbers.append(i)
                # we now want to cross out multiples of all i's that are primes, (hence the i at the end of range() to skip them).
                # we start at squares of i since anything below that has already been
                # eliminated by smaller i's.
                for j in range(i**2, n + 1, i): # for some reason, xrange here returns a StackOverflow error with
                    sieve[j] = False            # large ints like 1000000
        return prime_numbers


gen_primes(10000)

import time
start_time = time.time()
# main()
print("--- %s seconds ---" % (time.time() - start_time))

# gen_primes(39) now logs 0.00000190734863281 seconds.
# gen_primes(10000) now logs 0.000000953674316406 seconds.
# gen_primes(1000000) now logs 0.00000286102294922 seconds.
