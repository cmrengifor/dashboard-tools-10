import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

employees = [
    ("Alice Johnson", "Finance"), ("Bob Martinez", "HR"), ("Carol White", "IT"),
    ("David Lee", "Operations"), ("Emma Brown", "Sales"), ("Frank Wilson", "Finance"),
    ("Grace Chen", "HR"), ("Henry Davis", "IT"), ("Isabella Taylor", "Operations"),
    ("James Anderson", "Sales"), ("Karen Thomas", "Finance"), ("Liam Jackson", "HR"),
    ("Maria Harris", "IT"), ("Nathan Clark", "Operations"), ("Olivia Lewis", "Sales"),
    ("Peter Robinson", "Finance"), ("Quinn Walker", "HR"), ("Rachel Hall", "IT"),
    ("Samuel Young", "Operations"), ("Tina King", "Sales")
]
regions = ["North", "South", "East", "West", "Central"]
quarters = pd.date_range("2025-01-01", "2026-06-01", freq="QS")

rows = []
record_id = 1
for emp_name, dept in employees:
    emp_id = f"EMP{record_id:03d}"
    region = rng.choice(regions)
    tenure = round(rng.uniform(0.5, 12), 1)
    for quarter in quarters:
        eng = round(rng.uniform(45, 95), 1)
        sat = round(rng.uniform(40, 98), 1)
        nps_raw = round(rng.uniform(-80, 80), 0)
        if nps_raw >= 9:
            category = "Promoter"
        elif nps_raw >= 7:
            category = "Passive"
        else:
            category = "Detractor"
        # Align category to NPS scale
        if eng > 75:
            category = "Promoter"
        elif eng > 55:
            category = "Passive"
        else:
            category = "Detractor"
        nps = round(rng.uniform(-50, 80) if category == "Promoter" else
                    rng.uniform(-20, 30) if category == "Passive" else
                    rng.uniform(-80, 0), 0)
        rows.append({
            "employee_id": emp_id,
            "employee_name": emp_name,
            "department": dept,
            "survey_date": quarter.strftime("%Y-%m-%d"),
            "quarter": f"Q{quarter.quarter} {quarter.year}",
            "engagement_score": eng,
            "satisfaction_score": sat,
            "nps": int(nps),
            "category": category,
            "tenure_years": tenure,
            "region": region,
        })
    record_id += 1

df = pd.DataFrame(rows)
out = Path(__file__).parent / "data" / "engagement_data.csv"
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")
print(f"Avg Engagement: {df['engagement_score'].mean():.1f}")
print(f"Avg Satisfaction: {df['satisfaction_score'].mean():.1f}")
print(f"NPS: {df['nps'].mean():.0f}")
promoters = (df['category'] == 'Promoter').sum()
print(f"Promoter %: {promoters/len(df)*100:.1f}%")
