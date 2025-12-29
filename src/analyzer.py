from src.git_reader import get_git_commits
from src.checks.commit_frequency import analyze_commit_frequency
from src.checks.bad_messages import detect_bad_commit_messages
from src.checks.dead_days import detect_dead_days

class GitCommitAnalyzer:
    def run(self):
        commits = get_git_commits()

        return {
            "total_commits": len(commits),
            "commit_frequency": analyze_commit_frequency(commits),
            "bad_commit_messages": detect_bad_commit_messages(commits),
            "dead_days": detect_dead_days(commits)
        }
