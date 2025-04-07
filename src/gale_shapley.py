"""
Gale-Shapley Algorithm Implementation
For stable matching between hospitals and students (residents)

This implementation solves the hospital-resident matching problem
using the Gale-Shapley algorithm, where hospitals can have multiple positions
and both hospitals and students can have preferences.
"""

from time import process_time


def read_input_file(filename):
    """
    Read and parse the input file containing hospitals and students preferences.
    
    Parameters:
    - filename: Path to the input file
    
    Returns:
    - num_hospitals: Number of hospitals
    - num_students: Number of students
    - num_positions: List of positions available for each hospital
    - hospital_preferences: List of lists with each hospital's student preferences
    - student_preferences: List of dictionaries with each student's hospital preferences
    """
    try:
        with open(filename, "r") as f:
            # Process first line
            first_line = f.readline().split()
            num_hospitals = int(first_line[0])
            num_students = int(first_line[1])

            # Process second line - number of positions at each hospital
            second_line = f.readline().split()
            num_positions = [int(n) for n in second_line]
            
            # Process hospital preference lines
            hospital_preferences = []
            for i in range(num_hospitals):
                preferences = [int(student) for student in f.readline().split()]
                hospital_preferences.append(preferences)
            
            # Process student preference lines
            student_preferences = []
            for i in range(num_students):
                preferences = [int(hospital) for hospital in f.readline().split()]
                # Convert to dictionary for O(1) lookup of hospital rank
                pref_dict = {preferences[j]: j for j in range(len(preferences))}
                student_preferences.append(pref_dict)
                
    except FileNotFoundError:
        print(f"Error: Could not open file {filename}")
        return None
        
    return num_hospitals, num_students, num_positions, hospital_preferences, student_preferences


def gale_shapley(filename):
    """
    Runs the Gale-Shapley algorithm to find a stable matching between
    hospitals and students using preferences from the given input file.
    
    Parameters:
    - filename: Path to the input file
    
    Returns:
    - s_assigned_h: List where index i represents student i and the value
                    represents the hospital they are assigned to (or None)
    """
    start_time = process_time()
    
    # Read and parse input file
    result = read_input_file(filename)
    if result is None:
        return None
    
    num_hospitals, num_students, num_positions, hospital_preferences, student_preferences = result
    
    file_read_time = process_time()
    print(f"Time to read file = {file_read_time - start_time}")
    
    # Initialize student-to-hospital assignment to empty matching
    s_assigned_h = [None] * num_students
    
    # Make a copy of num_positions to track remaining positions
    remaining_positions = num_positions.copy()
    
    # Track current position in each hospital's preference list
    hosp_prefs_pointers = [0] * num_hospitals
    
    # Cache the length of each hospital's preference list for efficiency
    hosp_prefs_lengths = [len(hospital_preferences[i]) for i in range(num_hospitals)]
    
    # Maximum possible iterations to prevent infinite loops
    possible_iterations = sum(len(prefs) for prefs in hospital_preferences)
    num_iterations = 0
    
    # Main Gale-Shapley algorithm loop
    # We continue until we've tried all possible matches or reached iteration limit
    
    # Create a list of hospitals that still have students to propose to
    active_hospitals = list(range(num_hospitals))
    
    while active_hospitals and num_iterations < possible_iterations:
        # Get the next hospital with available positions and students to propose to
        h = active_hospitals[0]
        
        # If current hospital has more students to propose to
        if hosp_prefs_pointers[h] < hosp_prefs_lengths[h]:
            # Get the next student in hospital's preference list
            current_student = hospital_preferences[h][hosp_prefs_pointers[h]]
            
            # Move to the next student in hospital's preference list
            hosp_prefs_pointers[h] += 1
            
            # Check if this student has hospital h in their preference list
            hospital_rank = student_preferences[current_student].get(h, -1)
            
            # If student has hospital in their preference list
            if hospital_rank != -1:
                # If student is unmatched
                if s_assigned_h[current_student] is None:
                    # Assign student to hospital
                    s_assigned_h[current_student] = h
                    remaining_positions[h] -= 1
                    
                    # If hospital has no more positions, remove from active list
                    if remaining_positions[h] == 0:
                        active_hospitals.pop(0)
                
                # If student prefers this hospital to their current assignment
                elif hospital_rank < student_preferences[current_student].get(s_assigned_h[current_student]):
                    # Add current hospital back to active list if it was full
                    current_hospital = s_assigned_h[current_student]
                    if remaining_positions[current_hospital] == 0 and current_hospital not in active_hospitals:
                        active_hospitals.append(current_hospital)
                    
                    # Release position at previous hospital
                    remaining_positions[current_hospital] += 1
                    
                    # Assign to new hospital
                    s_assigned_h[current_student] = h
                    remaining_positions[h] -= 1
                    
                    # If hospital has no more positions, remove from active list
                    if remaining_positions[h] == 0:
                        active_hospitals.pop(0)
            
            # If the hospital has no more positions, remove it from active list
            if hosp_prefs_pointers[h] >= hosp_prefs_lengths[h] and h in active_hospitals:
                active_hospitals.remove(h)
            
            num_iterations += 1
        else:
            # Hospital has gone through all its preferences, remove from active list
            active_hospitals.pop(0)
    
    return s_assigned_h


if __name__ == "__main__":
    # Example usage
    result = gale_shapley("data/inputs/input1.txt")
    print(f"Matching result: {result}") 