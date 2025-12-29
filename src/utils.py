from datetime import datetime

def parse_git_date(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %z")

def format_day(date):
    return date.strftime("%Y-%m-%d")
