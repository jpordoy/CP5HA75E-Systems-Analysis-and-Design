# Assuming the schema is already populated as shown above

# Query to find all students with grades > 70% from a specific enrolment date
def find_students_with_good_grades(enrolment_date):
    students_with_good_grades = []
    for enrolment in enrolments:
        if enrolment["enrolment_date"] == enrolment_date:
            enrolment_id = enrolment["enrolment_id"]
            for grade in grades:
                if grade["enrolment_id"] == enrolment_id and grade["grade"] > 70:
                    student_id = enrolment["student_id"]
                    for student in students:
                        if student["student_id"] == student_id:
                            students_with_good_grades.append(student)
                            break
                    break
            break
    return students_with_good_grades

# Example usage
enrolment_date = "2023-01-15"
result_students = find_students_with_good_grades(enrolment_date)
for student in result_students:
    print(student)
