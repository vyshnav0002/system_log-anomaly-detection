from datetime import datetime

def classify_score(score):
    """
    IsolationForest:
    score > 0  -> normal
    score < 0  -> anomaly
    """
    if score > 0.1:
        return "HEALTHY", "LOW", "System is stable. No issues detected."
    elif score > 0:
        return "WARNING", "MEDIUM", "Minor unusual activity detected. Monitoring closely."
    else:
        return "CRITICAL", "HIGH", "Critical anomaly detected. Immediate investigation required."


def render_dashboard(status, risk, message, score):
    return f"""
┌──────────────────────────────────────────┐
│ AI LOG ANOMALY MONITOR                   │
├──────────────────────────────────────────┤
│ System Status  : {status}
│ Risk Level     : {risk}
│ Anomaly Score  : {score:.3f}
│ Last Checked   : {datetime.now().strftime('%d %b %Y, %H:%M:%S')}
├──────────────────────────────────────────┤
│ Assessment                              │
│ {message}
└──────────────────────────────────────────┘
"""
