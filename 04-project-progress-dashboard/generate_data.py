import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

project_names = [
    "ERP Migration", "CRM Rollout", "Cloud Infrastructure", "HR Portal",
    "Data Warehouse", "Mobile App", "Security Audit", "Process Automation",
    "BI Platform", "Customer Portal", "Compliance System", "API Gateway"
]
milestones = ["Planning", "Design", "Development", "Testing", "Deployment", "Review"]
team_members = [
    "Alice Chen", "Bob Martinez", "Carol Smith", "David Lee", "Eva Brown",
    "Frank Wilson", "Grace Kim", "Henry Davis", "Irene Lopez", "James White"
]
departments = ["Finance", "HR", "Operations", "Sales", "IT"]
statuses = ["On Track", "At Risk", "Delayed", "Complete"]
priorities = ["Critical", "High", "Medium", "Low"]
regions = ["North", "South", "East", "West", "Central"]

status_probs = [0.40, 0.25, 0.20, 0.15]
priority_probs = [0.15, 0.30, 0.35, 0.20]

start_base = pd.Timestamp("2025-01-01")
records = []
record_id = 1

for i, project in enumerate(project_names):
    dept = departments[i % len(departments)]
    region = regions[i % len(regions)]
    priority = rng.choice(priorities, p=priority_probs)
    for milestone in milestones:
        member = rng.choice(team_members)
        start_offset = int(rng.integers(0, 90))
        start_date = start_base + pd.Timedelta(days=start_offset)
        duration = int(rng.integers(14, 120))
        due_date = start_date + pd.Timedelta(days=duration)
        status = rng.choice(statuses, p=status_probs)
        if status == "Complete":
            completion_pct = 100
        elif status == "On Track":
            completion_pct = int(rng.integers(50, 90))
        elif status == "At Risk":
            completion_pct = int(rng.integers(25, 65))
        else:  # Delayed
            completion_pct = int(rng.integers(5, 45))

        records.append({
            "project_id": f"PRJ-{i+1:02d}",
            "project_name": project,
            "milestone": milestone,
            "team_member": member,
            "department": dept,
            "start_date": start_date.strftime("%Y-%m-%d"),
            "due_date": due_date.strftime("%Y-%m-%d"),
            "completion_pct": completion_pct,
            "status": status,
            "priority": priority,
            "region": region
        })
        record_id += 1

df = pd.DataFrame(records)
out = r"C:\Users\User\Project Program\dashboard-tools-10\04-project-progress-dashboard\data\project_progress_data.csv"
df.to_csv(out, index=False)

active = len(df[df['status'] != 'Complete']['project_name'].unique())
on_time_rate = round(len(df[df['status'].isin(['On Track', 'Complete'])]) / len(df) * 100, 1)
avg_completion = round(df['completion_pct'].mean(), 1)
at_risk = len(df[df['status'] == 'At Risk']['project_name'].unique())

print(f"Rows: {len(df)}")
print(f"Active Projects: {active}")
print(f"On-Time Rate %: {on_time_rate}")
print(f"Avg Completion %: {avg_completion}")
print(f"At-Risk Projects: {at_risk}")
