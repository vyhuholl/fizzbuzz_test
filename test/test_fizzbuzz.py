import unittest

from fizzbuzz import fizzbuzz


class TestInvalidInput(unittest.TestCase):
    def test_non_number_string(self):
        self.assertEqual(
            fizzbuzz.fizzbuzz('foo'),
            'Submit an integer number.'
            )

    def test_float_number(self):
        self.assertEqual(
            fizzbuzz.fizzbuzz('133.2'),
            'Submit an integer number.'
            )

    def test_zero(self):
        self.assertEqual(
            fizzbuzz.fizzbuzz('0'),
            'The number must be positive and non-zero.'
            )

    def test_negative(self):
        self.assertEqual(
            fizzbuzz.fizzbuzz('-1'),
            'The number must be positive and non-zero.'
            )


class TestValidInput(unittest.TestCase):
    def test_divisible_by_3(self):
        self.assertEqual(fizzbuzz.fizzbuzz('9'), 'Fizz!')

    def test_divisible_by_5(self):
        self.assertEqual(fizzbuzz.fizzbuzz('5'), 'Buzz!')

    def test_divisible_by_15(self):
        self.assertEqual(fizzbuzz.fizzbuzz('15'), 'FizzBuzz!')

    def test_non_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz.fizzbuzz('7'), 7)
        self.assertEqual(fizzbuzz.fizzbuzz('133'), 133)


if __name__ == '__main__':
    unittest.main()
