import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

periods = pd.date_range("2025-01-01", "2026-06-01", freq="MS")
departments = ["Finance", "HR", "IT", "Operations", "Sales"]
team_members = [
    "Alice Johnson", "Bob Martinez", "Carol White", "David Lee", "Emma Brown",
    "Frank Wilson", "Grace Chen", "Henry Davis", "Isabella Taylor", "James Anderson",
    "Karen Thomas", "Liam Jackson", "Maria Harris", "Nathan Clark", "Olivia Lewis"
]
data_types = ["Actual", "Forecast"]

rows = []
record_id = 1
for period in periods:
    for dept in departments:
        for data_type in data_types:
            member = rng.choice(team_members)
            base_revenue = {"Finance": 850_000, "HR": 320_000, "IT": 680_000,
                            "Operations": 920_000, "Sales": 1_100_000}[dept]
            trend = 1 + (period.month - 1) * 0.005
            noise = rng.uniform(0.90, 1.10)
            revenue = round(base_revenue * trend * noise, 2)

            ar = round(revenue * rng.uniform(0.15, 0.35), 2)
            ap = round(revenue * rng.uniform(0.10, 0.28), 2)
            collection_rate = round(rng.uniform(72, 98), 2)
            payment_rate = round(rng.uniform(75, 97), 2)
            dso = round(rng.uniform(25, 65), 1)
            dpo = round(rng.uniform(20, 55), 1)
            nwc = round(ar - ap + rng.uniform(-50_000, 100_000), 2)

            rows.append({
                "record_id": record_id,
                "period": period.strftime("%Y-%m-%d"),
                "year": period.year,
                "month": period.strftime("%b %Y"),
                "department": dept,
                "team_member": member,
                "data_type": data_type,
                "revenue": revenue,
                "ar_outstanding": ar,
                "ap_outstanding": ap,
                "collection_rate_pct": collection_rate,
                "payment_rate_pct": payment_rate,
                "dso": dso,
                "dpo": dpo,
                "net_working_capital": nwc,
            })
            record_id += 1

df = pd.DataFrame(rows)
out = Path(__file__).parent / "data" / "financial_kpis_data.csv"
df.to_csv(out, index=False)
print(f"Saved {len(df)} rows to {out}")
print(df[["revenue", "dso", "dpo", "net_working_capital"]].agg(["mean", "sum"]).round(2))
