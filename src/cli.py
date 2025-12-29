from src.analyzer import GitCommitAnalyzer
from src.report import console_report, save_reports

def main():
    analyzer = GitCommitAnalyzer()
    data = analyzer.run()

    console_report(data)
    save_reports(data)

if __name__ == "__main__":
    main()
