# Gale-Shapley Matching Algorithm Implementation

A Python implementation of the Gale-Shapley algorithm for solving the Hospital-Resident Matching Problem.

## Introduction

The Gale-Shapley algorithm is used to solve the stable matching problem, specifically in scenarios like matching students (residents) to hospitals. This implementation handles:

- Hospitals with multiple positions
- Hospitals and students with preference rankings
- Hospitals and students with incomplete preference lists (some may find others unacceptable)

The algorithm guarantees a stable matching, where no unmatched pair would both prefer each other over their current matching.

## Project Structure

```
gale_shapley_algorithm/
├── data/
│   ├── inputs/        # Input data files
│   └── solutions/     # Expected output files for test cases
├── src/
│   ├── gale_shapley.py   # Main algorithm implementation
│   └── example.py        # Example usage of the algorithm
├── tests/
│   └── test_gale_shapley.py  # Test suite
└── README.md
```

## How It Works

The implementation works as follows:

1. Parse the input file containing hospital and student preferences
2. Initialize an empty matching (all students unmatched)
3. Apply the Gale-Shapley algorithm:
   - Each hospital proposes to students in order of its preference list
   - Each student accepts if they're unmatched or if they prefer the new offer over their current match
   - Repeat until all hospitals have gone through their preferences or all positions are filled

## Input Format

The algorithm accepts input files in the following format:

```
<num_hospitals> <num_students>
<num_positions_hospital_0> <num_positions_hospital_1> ... <num_positions_hospital_n-1>
<hospital_0_preferences>
<hospital_1_preferences>
...
<hospital_n-1_preferences>
<student_0_preferences>
<student_1_preferences>
...
<student_m-1_preferences>
```

Where:
- Each line of hospital preferences contains student indices in order of preference
- Each line of student preferences contains hospital indices in order of preference

## Usage

Basic usage:

```python
from src.gale_shapley import gale_shapley

# Run the algorithm with an input file
matching = gale_shapley("data/inputs/input1.txt")
print(matching)
```

For a more comprehensive example, see `src/example.py`.

## Running Tests

To run the entire test suite:

```
python tests/test_gale_shapley.py
```

To run the tests using unittest:

```
python tests/test_gale_shapley.py --unittest
```

## Performance

The implementation is optimized to handle large-scale matching problems efficiently, with:

- O(1) lookup for preference rankings using dictionaries
- Efficient iteration over hospital preferences
- Early termination when a stable matching is found

## Example

For a small example with 3 hospitals and 5 students, where each hospital has 2 positions:

```
Hospital preferences:
Hospital 0: [0, 1, 2, 3, 4]
Hospital 1: [1, 0, 3, 4, 2]
Hospital 2: [2, 3, 1, 0, 4]

Student preferences:
Student 0: [0, 1, 2]
Student 1: [2, 1, 0]
Student 2: [1, 0, 2]
Student 3: [0, 2, 1]
Student 4: [2, 0, 1]
```

The algorithm produces a stable matching where each student is assigned to a hospital they find acceptable, and no student-hospital pair would mutually prefer each other over their current matching.

## References

1. Gale, D., & Shapley, L. S. (1962). College Admissions and the Stability of Marriage. The American Mathematical Monthly, 69(1), 9-15.
2. Roth, A. E. (1984). The Evolution of the Labor Market for Medical Interns and Residents: A Case Study in Game Theory. Journal of Political Economy, 92(6), 991-1016. 