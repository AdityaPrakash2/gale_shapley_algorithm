"""
Example usage of the Gale-Shapley algorithm.

This module demonstrates how to use the Gale-Shapley algorithm
for solving the hospital-resident matching problem.
"""

from src.gale_shapley import gale_shapley, read_input_file


def create_sample_input_file(filename):
    """
    Creates a sample input file for the Gale-Shapley algorithm.
    
    The format is:
    - First line: <num_hospitals> <num_students>
    - Second line: <positions per hospital>
    - Next num_hospitals lines: Each hospital's preferences 
    - Next num_students lines: Each student's preferences
    
    Parameters:
    - filename: The file to create
    """
    with open(filename, "w") as f:
        # 3 hospitals, 5 students
        f.write("3 5\n")
        
        # Each hospital has 2 positions
        f.write("2 2 2\n")
        
        # Hospital preferences (hospitals are 0-indexed)
        f.write("0 1 2 3 4\n")  # Hospital 0 preferences
        f.write("1 0 3 4 2\n")  # Hospital 1 preferences
        f.write("2 3 1 0 4\n")  # Hospital 2 preferences
        
        # Student preferences (students are 0-indexed)
        f.write("0 1 2\n")  # Student 0 preferences
        f.write("2 1 0\n")  # Student 1 preferences
        f.write("1 0 2\n")  # Student 2 preferences
        f.write("0 2 1\n")  # Student 3 preferences
        f.write("2 0 1\n")  # Student 4 preferences


def print_matching_result(matching):
    """
    Prints the matching results in a human-readable format.
    
    Parameters:
    - matching: List where index i represents student i and 
                the value represents the hospital they are assigned to
    """
    if matching is None:
        print("No matching found.")
        return
        
    print("\nMatching Results:")
    print("=================")
    
    # Group by hospital
    hospital_assignments = {}
    for student, hospital in enumerate(matching):
        if hospital is not None:
            if hospital not in hospital_assignments:
                hospital_assignments[hospital] = []
            hospital_assignments[hospital].append(student)
    
    # Print results by hospital
    for hospital in sorted(hospital_assignments.keys()):
        print(f"Hospital {hospital}: {hospital_assignments[hospital]}")
    
    # Print unmatched students
    unmatched = [student for student, hospital in enumerate(matching) if hospital is None]
    if unmatched:
        print(f"Unmatched students: {unmatched}")
    else:
        print("All students matched!")


def main():
    """Main function to demonstrate the Gale-Shapley algorithm"""
    # Create a sample input file
    sample_file = "../data/inputs/sample.txt"
    create_sample_input_file(sample_file)
    print(f"Created sample input file: {sample_file}")
    
    # Run the algorithm
    print("Running Gale-Shapley algorithm...")
    matching = gale_shapley(sample_file)
    
    # Print the results
    print_matching_result(matching)
    
    # Demonstrate accessing the parsed input data
    print("\nAccessing Raw Input Data:")
    print("========================")
    num_hospitals, num_students, num_positions, hospital_prefs, student_prefs = read_input_file(sample_file)
    
    print(f"Number of hospitals: {num_hospitals}")
    print(f"Number of students: {num_students}")
    print(f"Positions per hospital: {num_positions}")
    print(f"Hospital preferences: {hospital_prefs}")
    print(f"Student preferences: {student_prefs}")


if __name__ == "__main__":
    main() 