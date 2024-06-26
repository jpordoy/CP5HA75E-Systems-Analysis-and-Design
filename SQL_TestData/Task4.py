# Calculate average grade for all apprentices for each course
def calculate_average_grade_per_course():
    course_grades = {}
    for enrolment in enrolments:
        course_id = enrolment["course_id"]
        enrolment_id = enrolment["enrolment_id"]
        total_grades = 0
        count_grades = 0
        for grade in grades:
            if grade["enrolment_id"] == enrolment_id:
                total_grades += grade["grade"]
                count_grades += 1
        if count_grades > 0:
            average_grade = total_grades / count_grades
            if course_id in course_grades:
                course_grades[course_id]["average_grade"].append(average_grade)
            else:
                course_grades[course_id] = {
                    "average_grade": [average_grade],
                    "company_grades": {}
                }
    return course_grades

# Calculate average grade by company
def calculate_average_grade_by_company():
    company_grades = {}
    for apprentice in apprentices:
        company_id = apprentice["company_id"]
        if company_id not in company_grades:
            company_grades[company_id] = {
                "average_grade": [],
                "apprentices": []
            }
        company_grades[company_id]["apprentices"].append(apprentice["apprentice_id"])
    for company_id, data in company_grades.items():
        total_grades = 0
        count_grades = 0
        for apprentice_id in data["apprentices"]:
            for feedback_item in feedback:
                if feedback_item["apprentice_id"] == apprentice_id:
                    total_grades += apprentice["final_grade"]
                    count_grades += 1
        if count_grades > 0:
            average_grade = total_grades / count_grades
            data["average_grade"].append(average_grade)
    return company_grades

# Example usage
average_grades_per_course = calculate_average_grade_per_course()
average_grades_by_company = calculate_average_grade_by_company()
print("Average grades per course:", average_grades_per_course)
print("Average grades by company:", average_grades_by_company)
