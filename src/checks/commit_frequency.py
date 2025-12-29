from collections import defaultdict
from src.utils import parse_git_date, format_day

def analyze_commit_frequency(commits):
    freq = defaultdict(int)

    for c in commits:
        day = format_day(parse_git_date(c["date"]))
        freq[day] += 1

    return dict(freq)
