#a. Regex-dən istifadə edərək verilmiş veb server log faylından
# IP ünvanlarını, tarixləri və HTTP metodlarını çıxarın.
import re
import json
log_data="""192.168.1.10 - - [05/Dec/2024:10:15:45 +0000] "POST /login HTTP/1.1" 200 5320
192.168.1.11 - - [05/Dec/2024:10:16:50 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.15 - - [05/Dec/2024:10:17:02 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:18:10 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:19:30 +0000] "POST /login HTTP/1.1" 401 2340
192.168.1.11 - - [05/Dec/2024:10:20:45 +0000] "POST /login HTTP/1.1" 401 2340
10.0.0.16 - - [05/Dec/2024:10:21:03 +0000] "GET /home HTTP/1.1" 200 3020 """
pattern=r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<tarix>[^\]]+)] "(?P<method>GET|POST|DELETE|PUT|PATCH|OPTIONS|HEAD)'
matches=re.finditer(pattern,log_data)
for match in matches:
    ip =match.group("ip")
    date=match.group("tarix")
    metod=match.group("method")
    print(f'IP:{ip},Tarix:{date},Metod:{metod}')