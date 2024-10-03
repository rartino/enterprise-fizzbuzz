import unittest
from fizzbuzz.main import generate_fizzbuzz_sequence

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_sequence(self):
        result = generate_fizzbuzz_sequence(15)
        expected = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
