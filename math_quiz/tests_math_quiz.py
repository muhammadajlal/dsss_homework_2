import unittest
from math_quiz import random_Number_Generator, random_Operator_Generator, math_Problem_Solution_Generator


class TestMathGame(unittest.TestCase):

    def test_random_Number_Generator(self):
        """Test if random numbers generated are within the specified range."""
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_Number_Generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, "Test failed! Random number out of range.")

    def test_random_Operator_Generator(self):
        """Test if random operator generated is one of the specified operators."""
        operators = {'+', '-', '*'}
        for _ in range(100):  # Test a large number of operator generations
            operator = random_Operator_Generator()
            self.assertIn(operator, operators, f"Test failed! Invalid operator generated: {operator}")

    def test_math_Problem_Solution_Generator(self):
        """Test if math problem and solution are generated correctly based on inputs."""
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (6, 3, '-', '6 - 3', 3),
            (7, 4, '*', '7 * 4', 28),
            (8, 5, '+', '8 + 5', 13),
            (9, 6, '-', '9 - 6', 3),
            (10, 7, '*', '10 * 7', 70)

            ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_Problem_Solution_Generator(num1, num2, operator)
            self.assertEqual(problem, expected_problem, "Test failed! both problems are not same")
            self.assertEqual(answer, expected_answer, "Test failed ! both answers are not equal")

if __name__ == "__main__":
    unittest.main()
