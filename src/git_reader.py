import subprocess

def get_git_commits():
    """
    Returns list of commits:
    [{hash, author, date, message}]
    """
    cmd = [
        "git", "log",
        "--pretty=format:%H|%an|%ad|%s",
        "--date=iso"
    ]

    result = subprocess.run(
        cmd, capture_output=True, text=True
    )

    commits = []
    for line in result.stdout.split("\n"):
        parts = line.split("|", 3)
        if len(parts) == 4:
            commits.append({
                "hash": parts[0],
                "author": parts[1],
                "date": parts[2],
                "message": parts[3]
            })
    return commits
