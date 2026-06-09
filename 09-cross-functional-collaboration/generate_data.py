import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

departments = ["Finance", "HR", "IT", "Operations", "Sales"]
collab_types = ["Project", "Support", "Review", "Escalation", "Training"]
outcomes = ["Successful", "Partial", "Failed"]
outcome_probs = [0.60, 0.28, 0.12]
regions = ["North", "South", "East", "West", "Central"]
periods = pd.date_range("2025-01-01", "2026-06-01", freq="MS")

rows = []
collab_id = 1
for period in periods:
    for src in departments:
        for tgt in departments:
            if src == tgt:
                continue
            n_rows = int(rng.integers(2, 5))
            for _ in range(n_rows):
                collab_type = rng.choice(collab_types)
                outcome = rng.choice(outcomes, p=outcome_probs)
                interactions = int(rng.integers(5, 50))
                resolution_days = round(rng.uniform(1, 15), 1)
                satisfaction = round(rng.uniform(55, 98), 1)
                region = rng.choice(regions)
                rows.append({
                    "collab_id": f"COLLAB{collab_id:04d}",
                    "period": period.strftime("%Y-%m-%d"),
                    "year": period.year,
                    "month": period.strftime("%b %Y"),
                    "source_dept": src,
                    "target_dept": tgt,
                    "collaboration_type": collab_type,
                    "interactions_count": interactions,
                    "avg_resolution_days": resolution_days,
                    "satisfaction_score": satisfaction,
                    "outcome": outcome,
                    "region": region,
                })
                collab_id += 1

df = pd.DataFrame(rows)
out = Path(__file__).parent / "data" / "collaboration_data.csv"
out.parent.mkdir(exist_ok=True)
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")
print(f"Total Interactions: {df['interactions_count'].sum()}")
print(f"Avg Resolution Days: {df['avg_resolution_days'].mean():.1f}")
print(f"Avg Satisfaction: {df['satisfaction_score'].mean():.1f}")
print(f"Success Rate: {(df['outcome']=='Successful').sum()/len(df)*100:.1f}%")
