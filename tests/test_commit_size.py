from checks.commit_size import analyze_commit_size


def test_large_commit_detected():
    commits = [
        {
            "hash": "abcdef123",
            "files_changed": 15,
            "lines_added": 300,
            "lines_deleted": 300,
        }
    ]

    warnings = analyze_commit_size(commits)
    assert len(warnings) == 1
