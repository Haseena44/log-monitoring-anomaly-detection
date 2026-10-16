import re

LOG_FILE = "access.log"
# Sample log line: 127.0.0.1 - [10/Oct/2025] "GET /api HTTP/1.1" 500 123 1.2s

def parse_logs():
    errors = []
    slow_requests = []
    pattern = r'" (\d{3}).* (\d+\.\d+)s'

    with open(LOG_FILE, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                status = int(match.group(1))
                latency = float(match.group(2))
                if status >= 500:
                    errors.append(line.strip())
                if latency > 1.0: # flag >1 sec
                    slow_requests.append(line.strip())

    print(f"Found {len(errors)} server errors (5xx)")
    print(f"Found {len(slow_requests)} slow requests (>1s)")
    return errors, slow_requests

if __name__ == "__main__":
    parse_logs()
