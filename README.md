# Log Monitoring & Anomaly Detection Tool

Tool that parses web server logs and flags anomalies for faster troubleshooting.

## What it does
- Parses Nginx/Apache style logs
- Flags 5xx server errors
- Flags slow requests > 1 second (latency spike)
- Helps in faster root cause analysis

## Tech Stack
Python, Linux, Shell, Regex, Log Analysis, Git

## How to Run
```bash
python log_monitor.py
