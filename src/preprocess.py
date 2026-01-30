import re

def clean_log(log: str) -> str:
    log = re.sub(r'\d+', 'NUM', log)
    log = re.sub(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', 'IP', log)
    return log.lower().strip()

def load_and_clean_logs(path):
    with open(path, "r") as f:
        logs = f.readlines()
    return [clean_log(log) for log in logs]
