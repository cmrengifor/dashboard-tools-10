import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

employees = [
    "Alice Johnson", "Bob Martinez", "Carol White", "David Lee", "Emma Brown",
    "Frank Wilson", "Grace Chen", "Henry Davis", "Isabella Taylor", "James Anderson",
    "Karen Thomas", "Liam Jackson", "Maria Harris", "Nathan Clark", "Olivia Lewis",
    "Peter Robinson", "Quinn Walker", "Rachel Hall", "Samuel Young", "Tina King"
]
departments = ["Finance", "HR", "IT", "Operations", "Sales"]
training_types = ["Technical", "Soft Skills", "Leadership", "Compliance", "Safety"]
statuses = ["Completed", "In Progress", "Not Started", "Failed"]
trainings = {
    "Technical": ["Python for Analysts", "Excel Advanced", "Power BI Fundamentals", "SQL Basics"],
    "Soft Skills": ["Communication Skills", "Conflict Resolution", "Team Collaboration", "Presentation Skills"],
    "Leadership": ["Leadership Essentials", "Change Management", "Coaching Skills", "Strategic Thinking"],
    "Compliance": ["Data Privacy GDPR", "Anti-Corruption Policy", "Code of Conduct", "Health Regulations"],
    "Safety": ["Fire Safety", "Workplace Ergonomics", "First Aid", "Hazard Identification"]
}

rows = []
record_id = 1
for i, emp in enumerate(employees):
    dept = departments[i % len(departments)]
    n_trainings = rng.integers(18, 24)
    for _ in range(n_trainings):
        t_type = rng.choice(training_types)
        t_name = rng.choice(trainings[t_type])
        start_dt = pd.Timestamp("2025-01-01") + pd.Timedelta(days=int(rng.integers(0, 450)))
        duration_days = int(rng.integers(5, 45))
        complete_dt = start_dt + pd.Timedelta(days=duration_days)
        status_probs = [0.55, 0.20, 0.15, 0.10]
        status = rng.choice(statuses, p=status_probs)
        hours = round(rng.uniform(4, 40), 1)
        certified = bool(status == "Completed" and rng.random() > 0.25)
        score = round(rng.uniform(60, 100), 1) if status in ["Completed", "Failed"] else None
        if status == "Failed":
            score = round(rng.uniform(30, 59), 1)
        rows.append({
            "record_id": record_id,
            "employee_name": emp,
            "department": dept,
            "training_name": t_name,
            "training_type": t_type,
            "start_date": start_dt.strftime("%Y-%m-%d"),
            "completion_date": complete_dt.strftime("%Y-%m-%d") if status == "Completed" else None,
            "training_hours": hours,
            "certified": certified,
            "score": score,
            "status": status,
        })
        record_id += 1

df = pd.DataFrame(rows)
out = Path(__file__).parent / "data" / "training_development_data.csv"
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")

# KPI summary
completed = df[df["status"] == "Completed"]
print(f"Completion Rate: {len(completed)/len(df)*100:.1f}%")
print(f"Total Training Hours: {df['training_hours'].sum():.0f}")
print(f"Certified: {df['certified'].sum()}")
print(f"Avg Score: {df['score'].dropna().mean():.1f}")
