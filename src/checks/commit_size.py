from typing import List, Dict

MAX_FILES_CHANGED = 10
MAX_LINES_CHANGED = 500


def analyze_commit_size(commits: List[Dict]) -> List[str]:
    """
    Flags commits that are too large.
    Each commit dict must contain:
    - files_changed
    - lines_added
    - lines_deleted
    """
    warnings = []

    for commit in commits:
        total_lines = commit["lines_added"] + commit["lines_deleted"]

        if (
            commit["files_changed"] > MAX_FILES_CHANGED
            or total_lines > MAX_LINES_CHANGED
        ):
            warnings.append(
                f"Large commit detected: "
                f"{commit['files_changed']} files, "
                f"{total_lines} lines changed "
                f"(commit {commit['hash'][:7]})"
            )

    return warnings
