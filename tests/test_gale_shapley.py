"""
Test suite for the Gale-Shapley algorithm implementation.

This module contains tests for verifying the correctness of the 
hospital-resident matching algorithm implementation.
"""

import sys
import time
from time import process_time
import os
import unittest
import numpy as np

# Import the Gale-Shapley implementation
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.gale_shapley import gale_shapley


def test_problems(message, start_index, end_index, num_tests, num_correct, incorrect_tests):
    """
    Test problem indices from start_index up to and including end_index.
    
    Parameters:
    - message: Description of the test category
    - start_index: First test index to run
    - end_index: Last test index to run
    - num_tests: Running count of tests run
    - num_correct: Running count of correct tests
    - incorrect_tests: List of failed test indices
    
    Returns:
    - Updated (num_tests, num_correct, incorrect_tests)
    """
    print(message)
    for i in range(start_index, end_index + 1):
        num_tests += 1
        filename = f"data/inputs/input{i}.txt"
        print(f"Testing input file {filename}")
        solution_filename = f"data/solutions/solution{i}.txt"
        
        try:
            with open(solution_filename, "r") as solution_f:
                correct_answer = [None if i == "None" else int(i) for i in solution_f.readline().split()]
        
            s_time = process_time()
            your_answer = gale_shapley(filename)
            f_time = process_time()
            r_time = f_time - s_time
            print(f"Run time = {r_time}")
            
            if your_answer == correct_answer:
                print("Correct\n")
                num_correct += 1
            else:
                print("Incorrect")
                print(f"Your answer = {your_answer}")
                print(f"Correct answer = {correct_answer}\n")
                incorrect_tests.append(i)
        except Exception as e:
            print(f"Error testing {filename}: {str(e)}")
            incorrect_tests.append(i)
    
    return (num_tests, num_correct, incorrect_tests)


class TestGaleShapley(unittest.TestCase):
    """Test class for Gale-Shapley algorithm"""
    
    def test_basic_matching(self):
        """Test basic matching where each hospital has one position"""
        result = gale_shapley("data/inputs/input1.txt")
        with open("data/solutions/solution1.txt", "r") as f:
            expected = [None if i == "None" else int(i) for i in f.readline().split()]
        self.assertEqual(result, expected)
    
    def test_multiple_positions(self):
        """Test matching where hospitals have multiple positions"""
        result = gale_shapley("data/inputs/input6.txt")
        with open("data/solutions/solution6.txt", "r") as f:
            expected = [None if i == "None" else int(i) for i in f.readline().split()]
        self.assertEqual(result, expected)
    
    def test_more_students_than_positions(self):
        """Test matching where there are more students than positions"""
        result = gale_shapley("data/inputs/input10.txt")
        with open("data/solutions/solution10.txt", "r") as f:
            expected = [None if i == "None" else int(i) for i in f.readline().split()]
        self.assertEqual(result, expected)


def main():
    """Run the test suite on all test cases"""
    # Print message
    print("Checking Gale-Shapley implementation.")

    # Test for correctness
    num_tests = 0
    num_correct = 0
    incorrect_tests = []
    start_time = process_time()
    
    # Category 1: Basic matching
    message = """Testing 'basic' problems where each hospital
          has one position and there are the same number of
          hospitals as students.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 1, 5, num_tests, num_correct, incorrect_tests)

    # Category 2: Multiple positions
    message = """Testing problems where each hospital
          has more than one position, all hospitals have the same
          number of positions, and there are the same number of
          positions as students.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 6, 9, num_tests, num_correct, incorrect_tests)
    
    # Category 3: More students than positions
    message = """Testing problems where each hospital
          has more than one position, all hospitals have the same
          number of positions, but there are more students than positions.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 10, 13, num_tests, num_correct, incorrect_tests)

    # Category 4: Varying positions
    message = """Testing problems where each hospital
          has more than one position, hospitals have varying numbers of positions,
          and there are more students than positions.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 14, 17, num_tests, num_correct, incorrect_tests)

    # Category 5: More positions than students
    message = """Testing problems where each hospital
          has more than one position, hospitals have varying numbers of positions,
          and there are more positions than students.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 18, 21, num_tests, num_correct, incorrect_tests)

    # Category 6: Unacceptable preferences
    message = """Testing problems where hospitals have varying numbers of positions,
          there are more positions than students, and hospitals
          find some students unacceptable and some students find hospitals unacceptable.\n"""
    (num_tests, num_correct, incorrect_tests) = test_problems(message, 22, 25, num_tests, num_correct, incorrect_tests)

    # Category 7: Large test cases
    # message = """Testing large-scale problems"""
    # (num_tests, num_correct, incorrect_tests) = test_problems(message, 36, 37, num_tests, num_correct, incorrect_tests)

    # Summary
    end_time = process_time()
    print(f"Total tests: {num_tests}")
    print(f"Correct: {num_correct}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")
    
    if num_correct == num_tests:
        print("All tests passed successfully!")
    else:
        print(f"Some tests failed. Failed test indices: {incorrect_tests}")


if __name__ == "__main__":
    # Run either the full test suite or unittest
    if len(sys.argv) > 1 and sys.argv[1] == "--unittest":
        unittest.main(argv=['first-arg-is-ignored'])
    else:
        main() 