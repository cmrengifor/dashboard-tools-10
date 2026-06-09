import pandas as pd
import numpy as np
from datetime import date

rng = np.random.default_rng(42)

leaders = [
    "Alexandra Chen", "Marcus Williams", "Sofia Rodriguez", "James Okonkwo",
    "Priya Patel", "David Kim", "Laura Fernandez", "Thomas Novak"
]
departments = ["Operations", "Finance", "Sales", "Engineering", "HR"]
regions = ["North", "South", "East", "West", "Central"]

# Periods: Jan 2025 – Jun 2026 = 18 months
periods = pd.date_range("2025-01-01", "2026-06-01", freq="MS")

records = []
record_id = 1
for period in periods:
    for leader in leaders:
        dept = departments[leaders.index(leader) % len(departments)]
        region = regions[leaders.index(leader) % len(regions)]
        team_size = int(rng.integers(8, 25))
        turnover_rate = round(float(rng.uniform(2.0, 18.0)), 2)
        avg_performance = round(float(rng.uniform(58.0, 96.0)), 1)
        engagement = round(float(rng.uniform(55.0, 95.0)), 1)
        productivity_idx = round(float(rng.uniform(0.72, 1.35)), 3)
        coaching_hrs = round(float(rng.uniform(4.0, 28.0)), 1)
        promotions = int(rng.integers(0, 4))
        absenteeism = round(float(rng.uniform(1.0, 9.5)), 2)

        records.append({
            "record_id": record_id,
            "period": period.strftime("%b-%Y"),
            "year": period.year,
            "month": period.strftime("%b"),
            "leader_name": leader,
            "department": dept,
            "team_size": team_size,
            "turnover_rate_pct": turnover_rate,
            "avg_performance_score": avg_performance,
            "engagement_score": engagement,
            "productivity_index": productivity_idx,
            "coaching_hours": coaching_hrs,
            "promotions_count": promotions,
            "absenteeism_rate_pct": absenteeism,
            "region": region
        })
        record_id += 1

df = pd.DataFrame(records)
out_path = r"C:\Users\User\Project Program\dashboard-tools-10\10-leadership-impact-dashboard\data\leadership_impact_data.csv"
import os; os.makedirs(os.path.dirname(out_path), exist_ok=True)
df.to_csv(out_path, index=False)
print(f"Generated {len(df)} rows -> {out_path}")
print(df.head(3).to_string())
print("\nColumn dtypes:")
print(df.dtypes)
print(f"\nKPI previews:")
print(f"  Avg Leadership Score (performance): {df['avg_performance_score'].mean():.1f}")
print(f"  Avg Turnover Rate %: {df['turnover_rate_pct'].mean():.2f}")
print(f"  Avg Productivity Index: {df['productivity_index'].mean():.3f}")
print(f"  Total Coaching Hours: {df['coaching_hours'].sum():.1f}")
