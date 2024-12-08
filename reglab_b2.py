# Aşağıdakı sütunlarla CSV faylı yaradın:
# IP ünvanı, tarix, HTTP metodu və uğursuz cəhdlər.
import re
import csv

# Log məlumatları
log_data = """
192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020
"""

# Regex nümunəsi
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[^\]]+)\] "(?P<method>POST|GET|PUT|DELETE) .+ HTTP/1\.\d" (?P<status>\d{3})'

# Uğursuz girişlər üçün məlumatlar
failed_attempts = {}

# Log məlumatlarını analiz etmək
matches = re.finditer(pattern, log_data)
for match in matches:
    ip = match.group("ip")
    date = match.group("date")
    method = match.group("method")
    status = match.group("status")

    # Yalnız 401 status kodunu izləyirik
    if status == "401":
        if ip not in failed_attempts:
            failed_attempts[ip] = {"count": 0, "date": date, "method": method}
        failed_attempts[ip]["count"] += 1

# CSV faylına yaz
with open("failed_attempts.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    # Sütun başlıqları
    writer.writerow(["IP ünvanı", "Tarix", "HTTP metodu", "Uğursuz cəhdlər"])

    # Məlumatları yaz
    for ip, details in failed_attempts.items():
        writer.writerow([ip, details["date"], details["method"], details["count"]])

print("Uğursuz giriş cəhdləri 'failed_attempts.csv' faylına yazıldı.")
