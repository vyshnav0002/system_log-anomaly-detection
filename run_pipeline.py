from src.preprocess import clean_log, load_and_clean_logs
from src.feature_extraction import extract_features
from src.model import train_model
from src.file_watcher import follow
from src.status import classify_score, render_dashboard
from src.alert import flash_alert



train_logs = load_and_clean_logs("data/sample_logs.txt")
X, vectorizer = extract_features(train_logs)
model = train_model(X)

print("🚀 Real-time AI log monitoring started...\n")


for raw_log in follow("data/windows_system.log"):
    log = clean_log(raw_log)
    vec = vectorizer.transform([log])
    score = model.decision_function(vec)[0]

    status, risk, message = classify_score(score)

  
    if status == "CRITICAL":
        flash_alert("CRITICAL ANOMALY DETECTED!")

   
    print(render_dashboard(status, risk, message, score))

   
    if status != "HEALTHY":
        print("📄 Log Snippet:")
        print(log[:200])
        print("-" * 50)
    else:
        print(f"NORMAL | {log[:80]}")
