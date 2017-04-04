import unittest
from gen_primes import gen_primes


class GenPrimesTests(unittest.TestCase):
    def test_numbers_generated_are_really_primes(self):
        result = gen_primes(23)
        def is_prime(x):
            for n in xrange(2, x - 1):
                if x % n == 0:
                    return False
            else:
                return True
        for i in result:
            self.assertTrue(is_prime(i))

    def test_input_is_int(self):
        with self.assertRaises(ValueError, msg='Only positive integers are allowed as input'):
            gen_primes("1000")

    def test_input_is_positive_int(self):
        with self.assertRaises(ValueError, msg='Only integers greater than 0 are allowed'):
            gen_primes(-100)

    def test_it_does_not_omit_a_prime(self):
        result = gen_primes(23)
        self.assertEqual(len(result), 9, msg='Your function does not return all primes within the given range')

    def test_it_includes_input_if_input_is_prime(self):
        result = gen_primes(29)
        self.assertEqual(result[len(result) - 1], 29, msg='Your function should include the input number if it is a prime')


if __name__ == '__main__':
    unittest.main()
