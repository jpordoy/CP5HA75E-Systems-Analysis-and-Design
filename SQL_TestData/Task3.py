# Query to display timetable of an apprentice between 2 dates
def display_apprentice_timetable(apprentice_id, start_date, end_date):
    apprentice_timetable = {
        "apprentice_id": apprentice_id,
        "timetable": {
            "academic_commitments": [],
            "work_commitments": []
        }
    }
    # Mock data for academic and work commitments
    # Here we would query actual data from the system based on the apprentice_id and dates
    # For simplicity, using mock data
    apprentice_timetable["timetable"]["academic_commitments"].append({
        "date": "2023-01-20",
        "details": "Attend lecture on Data Structures"
    })
    apprentice_timetable["timetable"]["academic_commitments"].append({
        "date": "2023-01-25",
        "details": "Submit assignment on Algorithms"
    })
    apprentice_timetable["timetable"]["work_commitments"].append({
        "date": "2023-01-21",
        "details": "Work on project A, company ABC"
    })
    apprentice_timetable["timetable"]["work_commitments"].append({
        "date": "2023-01-23",
        "details": "Meeting with team at company XYZ"
    })
    return apprentice_timetable

# Example usage
apprentice_id = 1
start_date = "2023-01-15"
end_date = "2023-02-15"
result_timetable = display_apprentice_timetable(apprentice_id, start_date, end_date)
print(result_timetable)
