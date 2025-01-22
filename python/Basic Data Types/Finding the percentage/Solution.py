if __name__ == '__main__':
    # Read the number of students
    n = int(input())
    
    # Initialize an empty dictionary to store student marks
    student_marks = {}
    
    # Loop through the input to collect student names and their scores
    for _ in range(n):
        # Read the input where the first part is the name and the rest are scores
        name, *line = input().split()
        # Convert the scores to a list of floats
        scores = list(map(float, line))
        # Store the scores in the dictionary with the name as the key
        student_marks[name] = scores
    
    # Read the name of the student whose average score needs to be calculated
    query_name = input()
    
    # Calculate the average score for the queried student
    moy = sum(student_marks[query_name]) / len(student_marks[query_name])
    
    # Format the average to 2 decimal places
    moy = "%.2f" % moy
    
    # Print the formatted average
    print(moy)