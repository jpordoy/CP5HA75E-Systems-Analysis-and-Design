from datetime import datetime, timedelta

# List apprentices who completed their program within the last six months
def list_recently_completed_apprentices():
    today = datetime.today()
    six_months_ago = today - timedelta(days=180)
    recently_completed_apprentices = []
    for apprentice in apprentices:
        completion_date = datetime.strptime(apprentice["completion_date"], "%Y-%m-%d")
        if completion_date >= six_months_ago and completion_date <= today:
            apprentice_details = {
                "apprentice_name": apprentice["apprentice_name"],
                "completion_date": apprentice["completion_date"],
                "final_grade": apprentice["final_grade"]
            }
            for feedback_item in feedback:
                if feedback_item["apprentice_id"] == apprentice["apprentice_id"]:
                    apprentice_details["company_feedback"] = feedback_item["company_feedback"]
                    break
            recently_completed_apprentices.append(apprentice_details)
    return recently_completed_apprentices

# Example usage
recently_completed_apprentices = list_recently_completed_apprentices()
print("Apprentices who completed within last six months:")
for apprentice in recently_completed_apprentices:
    print(apprentice)
