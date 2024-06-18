def get_grade(score):
    """
    Determines the letter grade based on the score.
    :param score: int - the student's score
    :return: str - the letter grade
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def check_honors(gpa):
    """
    Determines if the student qualifies for honors based on GPA.
    :param gpa: float - the student's GPA
    :return: str - the honors designation, if any
    """
    if gpa >= 3.5:
        return "with honors"
    elif gpa >= 3.0:
        return "with distinction"
    else:
        return ""

def determine_result(score, gpa):
    """
    Combines the grade and honors status to print the final result.
    :param score: int - the student's score
    :param gpa: float - the student's GPA
    """
    grade = get_grade(score)  # Get the letter grade based on the score
    honors = check_honors(gpa)  # Check for honors based on the GPA
    
    # Print the final result based on grade and honors status
    if honors:
        print(f"The student scored {score}, which is a grade of {grade}, and graduated {honors}.")
    else:
        print(f"The student scored {score}, which is a grade of {grade}, and graduated without honors.")

if __name__ == "__main__":
    # Get user input for score and GPA
    score = int(input("Enter the student's score: "))
    gpa = float(input("Enter the student's GPA: "))
    
    # Determine and print the final result
    determine_result(score, gpa)
