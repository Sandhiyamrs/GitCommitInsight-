from datetime import time

WORK_START = time(9, 0)
WORK_END = time(18, 0)


def analyze_work_hours(commits):
    off_hours = []

    for commit in commits:
        commit_time = commit["date"].time()
        if commit_time < WORK_START or commit_time > WORK_END:
            off_hours.append(commit["hash"])

    return off_hours
