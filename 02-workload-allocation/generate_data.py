import pandas as pd
import numpy as np

rng = np.random.default_rng(42)

team_members = [
    "Alice Chen", "Bob Martinez", "Carol Smith", "David Lee", "Eva Brown",
    "Frank Wilson", "Grace Kim", "Henry Davis", "Irene Lopez", "James White",
    "Karen Taylor", "Luis Garcia", "Maria Johnson", "Nathan Clark", "Olivia Hall"
]
departments = ["Finance", "HR", "Operations", "Sales", "IT"]
task_types = ["Development", "Analysis", "Support", "Review", "Training"]
priorities = ["High", "Medium", "Low"]

member_dept = {m: departments[i % len(departments)] for i, m in enumerate(team_members)}

periods = pd.date_range("2025-01-01", "2026-06-01", freq="MS")
sprints = list(range(1, 11))

records = []
record_id = 1

for period in periods:
    period_str = period.strftime("%Y-%m")
    for member in team_members:
        sprint = rng.integers(1, 11)
        task_type = rng.choice(task_types)
        priority = rng.choice(priorities, p=[0.3, 0.45, 0.25])
        allocated_hours = int(rng.integers(60, 181))
        # utilization varies by priority
        base_util = {"High": 0.95, "Medium": 0.78, "Low": 0.62}[priority]
        util_noise = rng.normal(0, 0.12)
        utilization = min(max(base_util + util_noise, 0.4), 1.35)
        actual_hours = round(allocated_hours * utilization, 1)
        utilization_rate_pct = round(utilization * 100, 2)
        overloaded = 1 if utilization_rate_pct > 100 else 0

        records.append({
            "record_id": record_id,
            "period": period_str,
            "team_member": member,
            "department": member_dept[member],
            "task_type": task_type,
            "allocated_hours": allocated_hours,
            "actual_hours": actual_hours,
            "utilization_rate_pct": utilization_rate_pct,
            "priority": priority,
            "sprint": sprint,
            "overloaded": overloaded
        })
        record_id += 1

df = pd.DataFrame(records)
out = r"C:\Users\User\Project Program\dashboard-tools-10\02-workload-allocation\data\workload_data.csv"
df.to_csv(out, index=False)
print(f"Rows: {len(df)}")
print(df.head(3).to_string())
print(f"\noverloaded counts: {df['overloaded'].value_counts().to_dict()}")
print(f"utilization stats: min={df['utilization_rate_pct'].min():.1f} max={df['utilization_rate_pct'].max():.1f} avg={df['utilization_rate_pct'].mean():.1f}")
