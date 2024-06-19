def evaluate_employee(name, quality_of_work, punctuality, teamwork, years_of_service):
    # Initialize final evaluation and bonus eligibility
    final_evaluation = ""
    bonus_eligibility = False

    # Work Quality Evaluation
    if quality_of_work >= 90:
        work_evaluation = 'Excellent'
    elif 80 <= quality_of_work < 90:
        work_evaluation = 'Good'
    elif 70 <= quality_of_work < 80:
        work_evaluation = 'Satisfactory'
    else:
        work_evaluation = 'Needs Improvement'

    # Punctuality Evaluation
    if punctuality >= 95:
        punctuality_evaluation = 'Perfect Attendance'
    elif 85 <= punctuality < 95:
        punctuality_evaluation = 'Very Punctual'
    elif 75 <= punctuality < 85:
        punctuality_evaluation = 'Acceptable'
    else:
        punctuality_evaluation = 'Poor'

    # Teamwork Evaluation
    if teamwork >= 85:
        teamwork_evaluation = 'Great Team Player'
    elif 70 <= teamwork < 85:
        teamwork_evaluation = 'Good Team Player'
    else:
        teamwork_evaluation = 'Needs Improvement'

    # Overall Evaluation
    if work_evaluation == 'Excellent' and punctuality_evaluation != 'Poor' and teamwork_evaluation != 'Needs Improvement':
        final_evaluation = 'Outstanding Employee'
        # Check bonus eligibility for outstanding employees with 5+ years of service
        if years_of_service >= 5:
            bonus_eligibility = True
    elif work_evaluation == 'Good' and punctuality_evaluation != 'Poor' and teamwork_evaluation != 'Needs Improvement':
        final_evaluation = 'Valuable Employee'
        # Check bonus eligibility for valuable employees with 10+ years of service
        if years_of_service >= 10:
            bonus_eligibility = True
    elif work_evaluation == 'Satisfactory' and punctuality_evaluation != 'Poor' and teamwork_evaluation == 'Good Team Player':
        final_evaluation = 'Satisfactory Employee'
        # Check bonus eligibility for satisfactory employees with 15+ years of service
        if years_of_service >= 15:
            bonus_eligibility = True
    else:
        final_evaluation = 'Needs Improvement'

    # Output final result
    print(f"Employee: {name}")
    print(f"Quality of Work: {work_evaluation}")
    print(f"Punctuality: {punctuality_evaluation}")
    print(f"Teamwork: {teamwork_evaluation}")
    print(f"Overall Evaluation: {final_evaluation}")
    
    # Output bonus eligibility status
    if bonus_eligibility:
        print(f"{name} is eligible for a bonus.")
    else:
        print(f"{name} is not eligible for a bonus.")

# Example usage
employee_name = "Alice Johnson"
work_quality = 88
punctuality = 92
teamwork = 80
years_of_service = 12

# Evaluate the example employee
evaluate_employee(employee_name, work_quality, punctuality, teamwork, years_of_service)
