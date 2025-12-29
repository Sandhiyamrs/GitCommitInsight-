import os
from src.analyzer import GitCommitAnalyzer

def test_analyzer_runs():
    """
    Basic sanity test:
    Ensures analyzer runs inside a git repo
    and returns expected keys.
    """
    analyzer = GitCommitAnalyzer()
    data = analyzer.run()

    assert "total_commits" in data
    assert "commit_frequency" in data
    assert "bad_commit_messages" in data
    assert "dead_days" in data
    assert isinstance(data["total_commits"], int)
