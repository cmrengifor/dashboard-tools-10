import csv, json
rows = []
with open(r"C:\Users\User\Project Program\dashboard-tools-10\08-task-completion-dashboard\data\task_completion_data.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)
with open(r"C:\Users\User\Project Program\dashboard-tools-10\08-task-completion-dashboard\data\task_data.json", "w", encoding="utf-8") as f:
    json.dump(rows, f)
print(f"Written {len(rows)} rows, {len(rows[0])} cols")
