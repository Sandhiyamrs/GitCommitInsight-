import json

def console_report(data):
    print("\n📊 Git Commit Analysis Summary\n")
    print(f"Total Commits: {data['total_commits']}")
    print(f"Dead Days: {len(data['dead_days'])}")
    print(f"Bad Commit Messages: {len(data['bad_commit_messages'])}")

def save_reports(data):
    with open("output/report.json", "w") as f:
        json.dump(data, f, indent=4)

    with open("output/summary.txt", "w") as f:
        f.write(f"Total commits: {data['total_commits']}\n")
        f.write(f"Dead days: {len(data['dead_days'])}\n")
        f.write(f"Bad commits: {len(data['bad_commit_messages'])}\n")
