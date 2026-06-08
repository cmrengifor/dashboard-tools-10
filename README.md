# Dashboard-Tools-10: Leadership Intelligence Suite

A professional portfolio of **10 leadership and team management dashboards** built from a senior CFO perspective. Each dashboard delivers actionable visibility into people performance, operational efficiency, and organizational health — the metrics that drive executive decisions.

## Portfolio Overview

| # | Dashboard | Tool | CFO Value |
|---|---|---|---|
| 01 | [Team Performance Tracker](01-team-performance-tracker/) | Power BI | Monitor KPIs, productivity, and efficiency across team members |
| 02 | [Workload Allocation](02-workload-allocation/) | Excel | Task distribution, workload balance, and resource optimization |
| 03 | [Attendance & Punctuality](03-attendance-punctuality/) | Excel | Attendance rates, overtime, and punctuality for HR reporting |
| 04 | [Project Progress Dashboard](04-project-progress-dashboard/) | Power BI | Milestones, deadlines, and team progress against goals |
| 05 | [Financial KPIs Dashboard](05-financial-kpis-dashboard/) | Power BI | AP/AR financial data linked with team-level performance |
| 06 | [Training & Development Tracker](06-training-development-tracker/) | Excel | Employee skill development, certifications, and training ROI |
| 07 | [Employee Engagement Dashboard](07-employee-engagement-dashboard/) | Power BI | Survey scores, NPS, satisfaction trends, and retention signals |
| 08 | [Task Completion Dashboard](08-task-completion-dashboard/) | Excel | Completion rates, bottlenecks, and overdue task analysis |
| 09 | [Cross-Functional Collaboration](09-cross-functional-collaboration/) | Power BI | Inter-departmental collaboration metrics and workflow efficiency |
| 10 | [Leadership Impact Dashboard](10-leadership-impact-dashboard/) | Power BI + Excel | Leadership effectiveness via turnover, productivity, and engagement ROI |

## Strategic Design Principles (CFO Lens)

- **Financial linkage**: Dashboards 05 and 10 explicitly connect people metrics to financial outcomes (DSO, DPO, turnover cost, productivity ROI)
- **Consistent date range**: Jan 2025–Jun 2026 across all dashboards for cross-portfolio comparability
- **4 KPI cards per dashboard**: One glance = one decision. No dashboard noise.
- **Slicer-first design**: Department, region, and period filters on every dashboard for drill-down by any leadership level

## Tech Stack

| Layer | Tool |
|---|---|
| Data generation | Python (pandas, numpy) — seed=42 for reproducibility |
| Excel dashboards | ExcelMCP (COM interop) — pivot tables, charts, slicers |
| Power BI dashboards | Power BI Desktop — DAX measures, KPI cards, interactive visuals |
| Version control | Git / GitHub (`cmrengifor/dashboard-tools-10`) |

## Data

All datasets are synthetic, generated with `seed=42` for reproducibility. Each dashboard includes its own `data/` folder with a CSV file ready to load.

- **Period covered:** January 2025 – June 2026
- **Team size:** 15–20 employees across 5 departments
- **Regions:** Central, East, North, South, West

## Related Portfolio

- [dashboard-tools-10-ap-and-ar](https://github.com/cmrengifor/dashboard-tools-10-ap-and-ar) — Accounts Payable & Receivable suite (10 dashboards, Power BI + Excel)
