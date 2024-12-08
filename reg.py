import re
# result=dir(re)
# print(result)
#re.findall()
# result=re.findall("Turan",str)
# print(type(result))
# result=len(result)
# print(result)
# #re.split()
# netice=re.split(' ',str)
# print(netice)
# netice1=re.split("Sal",str)
# print(netice1)

#re.sub()

# resut1=re.sub(" ","-",str)
# resut2=re.sub("\s","+",str)
# print(resut1,resut2)

#re.search()
#result=re.search("Turan",str)
# print(result)
# res=result.span()
# print(res)
#result=result.start()
#result=result.end()
#result=result.group()
#result=result.string
# print(result)
#str='salam turan python saaamlam pyahon smlam 13594287'
# result=re.findall('[abc]',str)
# result=re.findall('[Sat]',str)
# result=re.findall("[a-z]",str)
# result=re.findall('[1-5]',str)
# result=re.findall('[0-48]',str) # 0,1,2,3,4 +8
# print(result)
# netice=re.findall("[^sal]",str)
# print(netice)
# result=re.findall("...",str)
# result=re.findall('py..on',str)
#result=re.findall("^s",str)
# result=re.findall("7$",str)
#str='salam turan python saaamlam pyahon smlam 13594287'
#result=re.findall("sa*m",str)
#result=re.findall("sa?m",str)
# result=re.findall("a{3}",str)
# result=re.findall("[0-9]{2}",str)
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Məlumatları saxlamaq üçün DataFrame
data = {
    "Tarix": [],
    "İşlərin sayı": []
}


# Məlumat əlavə edən funksiya
def yeni_melumat(tarix, say):
    data["Tarix"].append(tarix)
    data["İşlərin sayı"].append(say)


# Qrafik çəkmə funksiyası
def qrafik_cevir():
    df = pd.DataFrame(data)
    df['Tarix'] = pd.to_datetime(df['Tarix'])
    df = df.sort_values('Tarix')

    plt.plot(df['Tarix'], df['İşlərin sayı'], marker='o')
    plt.xlabel("Tarix")
    plt.ylabel("İşlərin sayı")
    plt.title("Motivasiya Qrafiki")
    plt.grid()
    plt.show()


# Məsələn, məlumat daxil etmək
yeni_melumat("2024-11-17", 5)
yeni_melumat("2024-11-18", 7)
yeni_melumat("2024-11-19", 6)

qrafik_cevir()
