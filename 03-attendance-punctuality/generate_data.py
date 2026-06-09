import pandas as pd
import numpy as np
import csv, json, os

rng = np.random.default_rng(42)

employees = [
    "Alice Chen", "Bob Martinez", "Carol Smith", "David Lee", "Eva Brown",
    "Frank Wilson", "Grace Kim", "Henry Davis", "Irene Lopez", "James White",
    "Karen Taylor", "Luis Garcia", "Maria Johnson", "Nathan Clark", "Olivia Hall",
    "Paul Adams", "Quinn Baker", "Rachel Evans", "Sam Foster", "Tina Green"
]
departments = ["Finance", "HR", "Operations", "Sales", "IT"]
statuses = ["Present", "Late", "Absent", "Leave"]
status_probs = [0.72, 0.12, 0.08, 0.08]

emp_dept = {e: departments[i % len(departments)] for i, e in enumerate(employees)}

periods = pd.date_range("2025-01-01", "2026-06-01", freq="MS")

records = []
record_id = 1

for period in periods:
    month = period.month
    year = period.year
    period_str = period.strftime("%Y-%m")
    for emp in employees:
        status = rng.choice(statuses, p=status_probs)
        scheduled_hours = 160
        if status == "Absent":
            actual_hours = 0
            overtime_hours = 0
            punctuality_score = 0
        elif status == "Leave":
            actual_hours = int(rng.integers(40, 100))
            overtime_hours = 0
            punctuality_score = int(rng.integers(70, 90))
        elif status == "Late":
            actual_hours = int(rng.integers(130, 160))
            overtime_hours = int(rng.integers(0, 10))
            punctuality_score = int(rng.integers(40, 70))
        else:  # Present
            actual_hours = int(rng.integers(155, 185))
            overtime_hours = max(0, actual_hours - 160)
            punctuality_score = int(rng.integers(75, 100))

        records.append({
            "record_id": record_id,
            "employee_name": emp,
            "department": emp_dept[emp],
            "date": period_str,
            "scheduled_hours": scheduled_hours,
            "actual_hours": actual_hours,
            "overtime_hours": overtime_hours,
            "status": status,
            "punctuality_score": punctuality_score,
            "month": month,
            "year": year
        })
        record_id += 1

df = pd.DataFrame(records)
out_csv = r"C:\Users\User\Project Program\dashboard-tools-10\03-attendance-punctuality\data\attendance_data.csv"
df.to_csv(out_csv, index=False)

# JSON for ExcelMCP
rows = [df.columns.tolist()] + df.values.tolist()
out_json = r"C:\Users\User\Project Program\dashboard-tools-10\03-attendance-punctuality\data\attendance_data.json"
with open(out_json, 'w') as f:
    json.dump([[str(v) if not isinstance(v, (int, float)) else v for v in row] for row in rows], f)

print(f"Rows: {len(df)}")
attendance_rate = round(df[df['status']=='Present']['employee_name'].count() / len(df) * 100, 1)
avg_ot = round(df['overtime_hours'].mean(), 1)
late_count = len(df[df['status']=='Late'])
absence_rate = round(df[df['status']=='Absent']['employee_name'].count() / len(df) * 100, 1)
print(f"Attendance Rate: {attendance_rate}%")
print(f"Avg Overtime Hours: {avg_ot}")
print(f"Late Arrival Count: {late_count}")
print(f"Absence Rate: {absence_rate}%")
