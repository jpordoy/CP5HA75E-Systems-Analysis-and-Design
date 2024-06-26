INSERT INTO student (student_id, student_name, student_email, student_address)
VALUES
(1, 'John Smith', 'john.smith@example.com', '123 Main St, London'),
(2, 'Emily Johnson', 'emily.johnson@example.com', '456 Elm St, London'),
(3, 'Michael Brown', 'michael.brown@example.com', '789 Oak St, London'),
(4, 'Emma Davis', 'emma.davis@example.com', '321 Maple St, London'),
(5, 'Daniel Wilson', 'daniel.wilson@example.com', '654 Pine St, London'),
(6, 'Sophia Lee', 'sophia.lee@example.com', '987 Cedar St, London'),
(7, 'James Taylor', 'james.taylor@example.com', '234 Birch St, London'),
(8, 'Olivia Clark', 'olivia.clark@example.com', '567 Walnut St, London'),
(9, 'Alexander Martinez', 'alexander.martinez@example.com', '890 Chestnut St, London'),
(10, 'Isabella Robinson', 'isabella.robinson@example.com', '432 Spruce St, London');


INSERT INTO enrolment (enrolment_id, student_id, course_id, enrolment_date)
VALUES
(1, 1, 101, '2023-01-15'),
(2, 2, 102, '2023-02-20'),
(3, 3, 103, '2023-03-10'),
(4, 4, 101, '2023-01-15'),
(5, 5, 102, '2023-02-20'),
(6, 6, 103, '2023-03-10'),
(7, 7, 101, '2023-01-15'),
(8, 8, 102, '2023-02-20'),
(9, 9, 103, '2023-03-10'),
(10, 10, 101, '2023-01-15');


INSERT INTO grades (grade_id, enrolment_id, grade)
VALUES
(1, 1, 85),
(2, 2, 78),
(3, 3, 92),
(4, 4, 80),
(5, 5, 87),
(6, 6, 75),
(7, 7, 82),
(8, 8, 79),
(9, 9, 88),
(10, 10, 83);


INSERT INTO apprentice (apprentice_id, apprentice_name, company_id, enrolment_date, completion_date, final_grade)
VALUES
(1, 'Mark Thompson', 201, '2023-01-10', '2023-07-10', 82),
(2, 'Sarah White', 202, '2023-02-15', '2023-08-15', 88),
(3, 'Ryan Harris', 203, '2023-03-20', '2023-09-20', 79),
(4, 'Jessica Hall', 201, '2023-01-10', '2023-07-10', 85),
(5, 'David Young', 202, '2023-02-15', '2023-08-15', 90),
(6, 'Amy King', 203, '2023-03-20', '2023-09-20', 76),
(7, 'Luke Scott', 201, '2023-01-10', '2023-07-10', 84),
(8, 'Julia Baker', 202, '2023-02-15', '2023-08-15', 86),
(9, 'Andrew Green', 203, '2023-03-20', '2023-09-20', 81),
(10, 'Sophie Adams', 201, '2023-01-10', '2023-07-10', 89);


INSERT INTO feedback (apprentice_id, company_feedback)
VALUES
(1, 'Mark performed exceptionally well throughout the apprenticeship period.'),
(2, 'Sarah showed great dedication and improvement in her skills.'),
(3, 'Ryan struggled initially but showed steady progress over time.'),
(4, 'Jessica consistently met expectations and contributed positively.'),
(5, 'David exceeded expectations with high-quality work and commitment.'),
(6, 'Amy needed more support initially but showed improvement.'),
(7, 'Luke demonstrated strong analytical skills and problem-solving abilities.'),
(8, 'Julia was proactive and demonstrated leadership qualities.'),
(9, 'Andrew showed excellent teamwork and communication skills.'),
(10, 'Sophie consistently delivered outstanding results and showed great initiative.');




SELECT s.student_id, s.student_name, g.grade
FROM enrolment e
JOIN student s ON e.student_id = s.student_id
JOIN grades g ON e.enrolment_id = g.enrolment_id
WHERE g.grade > 70
AND e.enrolment_date >= '2023-01-01'; -- Replace with your chosen enrolment date



SELECT event_type, event_date, event_description
FROM timetable
WHERE apprentice_id = 'your_apprentice_id'
AND event_date BETWEEN '2023-01-01' AND '2023-06-30'; -- Replace with your chosen date range


-- Average grade for each course
SELECT c.course_id, c.course_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN enrolment e ON g.enrolment_id = e.enrolment_id
JOIN course c ON e.course_id = c.course_id
GROUP BY c.course_id, c.course_name;

-- Average grade by company
SELECT c.company_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN enrolment e ON g.enrolment_id = e.enrolment_id
JOIN company c ON e.company_id = c.company_id
GROUP BY c.company_name;


SELECT a.apprentice_id, a.apprentice_name, a.completion_date, a.final_grade, f.company_feedback
FROM apprentice a
JOIN feedback f ON a.apprentice_id = f.apprentice_id
WHERE a.completion_date > '2023-06-30'; -- Replace with your chosen date range


