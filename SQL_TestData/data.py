# Schema for the tables used in the examples
# Student Table
students = [
    {"student_id": 1, "student_name": "John Smith", "student_email": "john.smith@example.com", "student_address": "123 Main St, London"},
    {"student_id": 2, "student_name": "Emily Johnson", "student_email": "emily.johnson@example.com", "student_address": "456 Elm St, London"},
    {"student_id": 3, "student_name": "Michael Brown", "student_email": "michael.brown@example.com", "student_address": "789 Oak St, London"},
    {"student_id": 4, "student_name": "Emma Davis", "student_email": "emma.davis@example.com", "student_address": "321 Maple St, London"},
    {"student_id": 5, "student_name": "Daniel Wilson", "student_email": "daniel.wilson@example.com", "student_address": "654 Pine St, London"},
    {"student_id": 6, "student_name": "Sophia Lee", "student_email": "sophia.lee@example.com", "student_address": "987 Cedar St, London"},
    {"student_id": 7, "student_name": "James Taylor", "student_email": "james.taylor@example.com", "student_address": "234 Birch St, London"},
    {"student_id": 8, "student_name": "Olivia Clark", "student_email": "olivia.clark@example.com", "student_address": "567 Walnut St, London"},
    {"student_id": 9, "student_name": "Alexander Martinez", "student_email": "alexander.martinez@example.com", "student_address": "890 Chestnut St, London"},
    {"student_id": 10, "student_name": "Isabella Robinson", "student_email": "isabella.robinson@example.com", "student_address": "432 Spruce St, London"}
]

# Enrolment Table
enrolments = [
    {"enrolment_id": 1, "student_id": 1, "course_id": 101, "enrolment_date": "2023-01-15"},
    {"enrolment_id": 2, "student_id": 2, "course_id": 102, "enrolment_date": "2023-02-20"},
    {"enrolment_id": 3, "student_id": 3, "course_id": 103, "enrolment_date": "2023-03-10"},
    {"enrolment_id": 4, "student_id": 4, "course_id": 101, "enrolment_date": "2023-01-15"},
    {"enrolment_id": 5, "student_id": 5, "course_id": 102, "enrolment_date": "2023-02-20"},
    {"enrolment_id": 6, "student_id": 6, "course_id": 103, "enrolment_date": "2023-03-10"},
    {"enrolment_id": 7, "student_id": 7, "course_id": 101, "enrolment_date": "2023-01-15"},
    {"enrolment_id": 8, "student_id": 8, "course_id": 102, "enrolment_date": "2023-02-20"},
    {"enrolment_id": 9, "student_id": 9, "course_id": 103, "enrolment_date": "2023-03-10"},
    {"enrolment_id": 10, "student_id": 10, "course_id": 101, "enrolment_date": "2023-01-15"}
]

# Grades Table
grades = [
    {"grade_id": 1, "enrolment_id": 1, "grade": 85},
    {"grade_id": 2, "enrolment_id": 2, "grade": 78},
    {"grade_id": 3, "enrolment_id": 3, "grade": 92},
    {"grade_id": 4, "enrolment_id": 4, "grade": 80},
    {"grade_id": 5, "enrolment_id": 5, "grade": 87},
    {"grade_id": 6, "enrolment_id": 6, "grade": 75},
    {"grade_id": 7, "enrolment_id": 7, "grade": 82},
    {"grade_id": 8, "enrolment_id": 8, "grade": 79},
    {"grade_id": 9, "enrolment_id": 9, "grade": 88},
    {"grade_id": 10, "enrolment_id": 10, "grade": 83}
]

# Apprentice Table
apprentices = [
    {"apprentice_id": 1, "apprentice_name": "Mark Thompson", "company_id": 201, "enrolment_date": "2023-01-10", "completion_date": "2023-07-10", "final_grade": 82},
    {"apprentice_id": 2, "apprentice_name": "Sarah White", "company_id": 202, "enrolment_date": "2023-02-15", "completion_date": "2023-08-15", "final_grade": 88},
    {"apprentice_id": 3, "apprentice_name": "Ryan Harris", "company_id": 203, "enrolment_date": "2023-03-20", "completion_date": "2023-09-20", "final_grade": 79},
    {"apprentice_id": 4, "apprentice_name": "Jessica Hall", "company_id": 201, "enrolment_date": "2023-01-10", "completion_date": "2023-07-10", "final_grade": 85},
    {"apprentice_id": 5, "apprentice_name": "David Young", "company_id": 202, "enrolment_date": "2023-02-15", "completion_date": "2023-08-15", "final_grade": 90},
    {"apprentice_id": 6, "apprentice_name": "Amy King", "company_id": 203, "enrolment_date": "2023-03-20", "completion_date": "2023-09-20", "final_grade": 76},
    {"apprentice_id": 7, "apprentice_name": "Luke Scott", "company_id": 201, "enrolment_date": "2023-01-10", "completion_date": "2023-07-10", "final_grade": 84},
    {"apprentice_id": 8, "apprentice_name": "Julia Baker", "company_id": 202, "enrolment_date": "2023-02-15", "completion_date": "2023-08-15", "final_grade": 86},
    {"apprentice_id": 9, "apprentice_name": "Andrew Green", "company_id": 203, "enrolment_date": "2023-03-20", "completion_date": "2023-09-20", "final_grade": 81},
    {"apprentice_id": 10, "apprentice_name": "Sophie Adams", "company_id": 201, "enrolment_date": "2023-01-10", "completion_date": "2023-07-10", "final_grade": 89}
]

# Feedback Table
feedback = [
    {"apprentice_id": 1, "company_feedback": "Mark performed exceptionally well throughout the apprenticeship period."},
    {"apprentice_id": 2, "company_feedback": "Sarah showed great dedication and improvement in her skills."},
    {"apprentice_id": 3, "company_feedback": "Ryan struggled initially but showed steady progress over time."},
    {"apprentice_id": 4, "company_feedback": "Jessica consistently met expectations and contributed positively."},
    {"apprentice_id": 5, "company_feedback": "David exceeded expectations with high-quality work and commitment."},
    {"apprentice_id": 6, "company_feedback": "Amy needed more support initially but showed improvement."},
    {"apprentice_id": 7, "company_feedback": "Luke demonstrated strong analytical skills and problem-solving abilities."},
    {"apprentice_id": 8, "company_feedback": "Julia was proactive and demonstrated leadership qualities."},
    {"apprentice_id": 9, "company_feedback": "Andrew showed excellent teamwork and communication skills."},
    {"apprentice_id": 10, "company_feedback": "Sophie consistently delivered outstanding results and showed great initiative."}
]
