#5-dən çox uğursuz giriş cəhdi olan
# hər hansı IP ünvanlarını müəyyən edin
# və onları JSON faylında saxlayın.
import re

log_data = """
192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020
"""

pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "(?P<method>POST|GET|PUT|DELETE) .+ HTTP/1\.\d" (?P<status>\d{3})'

failed_attempts = {}

matches = re.finditer(pattern, log_data)
for match in matches:
    ip = match.group("ip")
    status = match.group("status")

    if status == "401":
        if ip not in failed_attempts:
            failed_attempts[ip] = 0
        failed_attempts[ip] += 1

print("Uğursuz girişlər:")
print(failed_attempts)
