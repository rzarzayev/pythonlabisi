import re

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
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[.*\] "(?P<method>POST|GET|PUT|DELETE) .+ HTTP/1\.\d" (?P<status>\d{3})'

# Uğursuz girişlərin saxlanması üçün lüğət
failed_attempts = {}

# Log məlumatlarını analiz etmək
matches = re.finditer(pattern, log_data)
for match in matches:
    ip = match.group("ip")
    status = match.group("status")

    # Yalnız status 401 olanları əlavə et
    if status == "401":
        if ip not in failed_attempts:
            failed_attempts[ip] = 0
        failed_attempts[ip] += 1

# Nəticəni mətn faylına yaz
with open("failed_attempts.txt", "w",encoding='utf-8') as file:
    for ip, count in failed_attempts.items():
        file.write(f"{ip}: {count} uğursuz giriş cəhdi\n")

print("Uğursuz giriş cəhdlərinin sayı və IP ünvanları 'failed_attempts.txt' faylına yazıldı.")
