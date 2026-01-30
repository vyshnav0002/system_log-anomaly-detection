# AI Log Anomaly Detection

Real-time AI-based system log anomaly detection using **Isolation Forest**.  
This project monitors system logs, detects anomalies, and alerts the user in real-time using a CLI dashboard.

---

## Features

- Continuous monitoring of system logs
- Detects anomalies using machine learning
- Displays real-time alerts in the terminal
- Demo mode included with pre-filled fake logs for showcasing

---

## Project Structure

system_log-anomaly-detection/
├── src/ # Python modules (preprocess, feature_extraction, model, file_watcher)
├── data/ # Demo logs
│ └── demo_logs.log
├── run_pipeline.py # Main pipeline script
├── README.md
└── requirements.txt


---

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/vyshnav0002/system_log-anomaly-detection.git
cd system_log-anomaly-detection


Create and activate a virtual environment (optional but recommended)

python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux / Mac


Install dependencies

pip install -r requirements.txt

Running the Demo

Run the pipeline

python run_pipeline.py


Inject a demo anomaly in another terminal

cmd /c echo CRITICAL ERROR: Kernel panic detected >> data/demo_logs.log


Observe the output

Normal logs appear in GREEN

Critical anomalies trigger RED alerts, blinking warning, and anomaly score

Demo Logs

data/demo_logs.log contains sample logs for demonstration purposes.
You can edit or add logs to simulate different scenarios.

