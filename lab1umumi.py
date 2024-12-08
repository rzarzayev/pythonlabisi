'''
Nəticə etibarilə
verilən:
server_logs.txt
tapşırıqda istənilən:
failed_logins.json          - Bu fayl 5-dən çox uğursuz giriş cəhdi olan IP ünvanlarını saxlamalıdır.

threat_ips.json             - Bu fayl veb server log və təhdid kəşfiyyatı arasında uyğun gələn IP ünvanlarını saxlamalıdır.

combined_security_data.json - Bu fayl uğursuz girişləri və təhdid kəşfiyyatı IP-lərini birləşdirməlidir.

log_analysis.txt            - Bu faylda çıxarılan IP ünvanları və onların uğursuz cəhdləri olmalıdır.

log_analysis.csv            - Bu fayl cədvəl formatında çıxarılan məlumatları özündə saxlamalıdır.
'''



import re
import json
import csv
from collections import defaultdict
log_file = "C:Users\AG\Desktop\Yeni qovluq\server_logs.txt"
threat_ips = ["192.168.1.11", "10.0.0.15"]
pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>[^\]]+)\] "(?P<method>GET|POST|PUT|DELETE) .+ HTTP/1\.\d" (?P<status>\d{3})'
failed_attempts = defaultdict(int)
detailed_logs = []
try:
    with open(log_file, "r", encoding="utf-8") as file:
        log_data = file.readlines()
except FileNotFoundError:
    print(f"Fayl tapılmadı: {log_file}. Zəhmət olmasa faylı əlavə edin və yenidən cəhd edin.")
    exit()
# Log məlumatlarının analizi
for line in log_data:
    match = re.search(pattern, line)
    if match:
        ip = match.group("ip")
        date = match.group("date")
        method = match.group("method")
        status = match.group("status")
        detailed_logs.append({"ip": ip, "date": date, "method": method, "status": status})

        # Uğursuz girişləri toplamaq
        if status == "401":  # 401 - Ugursuz giris
            failed_attempts[ip] += 1
frequent_failed_logins = {ip: count for ip, count in failed_attempts.items() if count > 5}

threat_matches = {ip: count for ip, count in failed_attempts.items() if ip in threat_ips}
# Bütün məlumatların birləşdirilməsi
combined_data = {
    "frequent_failed_logins": frequent_failed_logins,
    "threat_matches": threat_matches,
}
# a. 5-dən çox ugursuz giriş edenlər ücün JSON
with open("failed_logins.json", "w", encoding="utf-8") as file:
    json.dump(frequent_failed_logins, file, indent=4)
# b. Təhdid IP-ler üçün JSON
with open("threat_ips.json", "w", encoding="utf-8") as file:
    json.dump(threat_matches, file, indent=4)

# c. Birleşdirilmiş melumat üçün JSON
with open("combined_security_data.json", "w", encoding="utf-8") as file:
    json.dump(combined_data, file, indent=4)
# d. Ugursuz giriş cehdlərinin mətn faylı
with open("log_analysis.txt", "w", encoding="utf-8") as file:
    for ip, count in failed_attempts.items():
        file.write(f"{ip}: {count} uğursuz giriş cəhdi\n")

# e. CSV fayl
with open("log_analysis.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["IP ünvanı", "Tarix", "HTTP metodu", "Uğursuz cəhdlər"])
    for log in detailed_logs:
        csv_writer.writerow([log["ip"], log["date"], log["method"], failed_attempts.get(log["ip"], 0)])

# Uğur mesajı
print("Bütün analizlər tamamlandı. Aşağıdakı fayllar yaradıldı:")
print("- failed_logins.json")
print("- threat_ips.json")
print("- combined_security_data.json")
print("- log_analysis.txt")
print("- log_analysis.csv")
