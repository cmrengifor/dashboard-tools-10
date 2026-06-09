import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

assignees = [
    "Alice Johnson", "Bob Martinez", "Carol White", "David Lee", "Emma Brown",
    "Frank Wilson", "Grace Chen", "Henry Davis", "Isabella Taylor", "James Anderson",
    "Karen Thomas", "Liam Jackson", "Maria Harris", "Nathan Clark", "Olivia Lewis"
]
departments = ["Finance", "HR", "IT", "Operations", "Sales"]
dept_map = {a: departments[i % len(departments)] for i, a in enumerate(assignees)}
priorities = ["Critical", "High", "Medium", "Low"]
priority_probs = [0.10, 0.30, 0.40, 0.20]
statuses = ["Completed", "In Progress", "Overdue", "Cancelled"]
status_probs = [0.55, 0.18, 0.17, 0.10]

task_names = [
    "Quarterly Report", "Budget Review", "System Upgrade", "Team Meeting",
    "Client Presentation", "Data Migration", "Compliance Audit", "Performance Review",
    "Process Improvement", "Risk Assessment", "Product Launch", "Training Session",
    "Contract Negotiation", "Vendor Evaluation", "Security Patch",
    "Dashboard Setup", "Policy Update", "Stakeholder Report", "Code Review", "Market Analysis"
]

rows = []
for task_id in range(1, 551):
    assignee = rng.choice(assignees)
    dept = dept_map[assignee]
    priority = rng.choice(priorities, p=priority_probs)
    status = rng.choice(statuses, p=status_probs)
    sprint = int(rng.integers(1, 11))
    task_name = rng.choice(task_names)

    assigned_date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=int(rng.integers(0, 450)))
    duration = int(rng.integers(3, 30))
    due_date = assigned_date + pd.Timedelta(days=duration)

    if status == "Completed":
        # some complete on time, some late
        extra = int(rng.integers(-2, 8))
        completion_date = due_date + pd.Timedelta(days=extra)
        is_overdue = extra > 0
        days_overdue = max(0, extra)
        days_to_complete = (completion_date - assigned_date).days
    elif status == "Overdue":
        extra = int(rng.integers(1, 20))
        completion_date = None
        is_overdue = True
        days_overdue = extra
        days_to_complete = None
    else:
        completion_date = None
        is_overdue = False
        days_overdue = 0
        days_to_complete = None

    rows.append({
        "task_id": f"TASK{task_id:04d}",
        "task_name": task_name,
        "assignee": assignee,
        "department": dept,
        "assigned_date": assigned_date.strftime("%Y-%m-%d"),
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completion_date": completion_date.strftime("%Y-%m-%d") if completion_date else None,
        "status": status,
        "priority": priority,
        "is_overdue": is_overdue,
        "days_overdue": days_overdue,
        "sprint": sprint,
    })

df = pd.DataFrame(rows)
out = Path(__file__).parent / "data" / "task_completion_data.csv"
out.parent.mkdir(exist_ok=True)
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")

completed = df[df["status"] == "Completed"]
print(f"Completion Rate: {len(completed)/len(df)*100:.1f}%")
print(f"Overdue Tasks: {df['is_overdue'].sum()}")
on_time = completed[~completed['is_overdue']]
print(f"On-Time Rate: {len(on_time)/len(df)*100:.1f}%")
avg_days = df['days_to_complete'].dropna().mean()
print(f"Avg Days to Complete: {avg_days:.1f}")
