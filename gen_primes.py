def gen_primes(n):
    # From the tests, we require input n to be an int only, and a positive one.
    if not isinstance(n, int):
        raise ValueError("Only positive integers are allowed as input")
    elif n < 1:
        raise ValueError("Only integers greater than 0 are allowed")
    else:
        """Generate prime numbers from 1 up to the specified number n."""
        prime_numbers = []
        for i in range(2, n + 1):
            prime = True
            # This filters out non-primes. A prime number is not divisible
            # by any number other than itself
            for j in range(2, i - 1):
                if i % j == 0:
                    prime = False
            if prime:   # if prime is not false.
                prime_numbers.append(i)    # trailing comma so that they are in a line
        return prime_numbers

# test case n
# print gen_primes(29)
