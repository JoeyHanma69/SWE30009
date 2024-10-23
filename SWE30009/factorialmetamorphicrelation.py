import unittest
from factorial import recur_factorial

class TestFactorialMetamorphicRelations(unittest.TestCase):
    def test_small_values(self):
        # Test with small integers to verify basic correctness
        self.assertEqual(recur_factorial(1), 1, "Factorial of 1 should be 1")
        self.assertEqual(recur_factorial(2), 2, "Factorial of 2 should be 2")
        self.assertEqual(recur_factorial(3), 6, "Factorial of 3 should be 6")

    def test_medium_values(self):
        # Test with medium-sized integers to ensure computational accuracy
        self.assertEqual(recur_factorial(10), 3628800, "Factorial of 10 should be 3628800")
        self.assertEqual(recur_factorial(11), 39916800, "Factorial of 11 should be 39916800")
        self.assertEqual(recur_factorial(12), 479001600, "Factorial of 12 should be 479001600")

    def test_large_values(self):
        # Test with larger integers to check for performance and handling of larger calculations
        self.assertEqual(recur_factorial(20), 2432902008176640000, "Factorial of 20 should be 2432902008176640000")
        self.assertEqual(recur_factorial(21), 51090942171709440000, "Factorial of 21 should be 51090942171709440000")
        self.assertEqual(recur_factorial(22), 1124000727777607680000, "Factorial of 22 should be 1124000727777607680000")

    def test_edge_case_zero(self):
        # Specifically test the behavior at the boundary condition of zero
        self.assertEqual(recur_factorial(0), 1, "Factorial of 0 should be 1")

    def test_sequence_test(self):
        # Verify sequential computation by iterating through a sequence of numbers
        expected_results = [120, 720, 5040, 40320, 362880]  # Factorials for 5 through 9
        for i, result in enumerate(expected_results, start=5):
            with self.subTest(i=i):
                self.assertEqual(recur_factorial(i), result, f"Factorial of {i} should be {result}")

if __name__ == "__main__":
    unittest.main()
