import re
import datetime

print("О чем мне вам напомнить?")
message = input()
text1 = re.findall(r"[^0-9.;:-]", message) #доработать
text = ''.join(text1)
#text = text[:-2]
print(text)
#text = re.findall(r'^январ.|^феврал.|^март.|^апрел.|^ма.|^июн.|^июл.|^август.|^сентябр.|^октябрь.|^ноябр.|^декабр.', message)
print(text)

date1 = re.findall(r"[0-9][0-9][.,-][0-9][0-9][.,-]?[0-9]?[0-9]?[0-9]?[0-9]?", message)
date = ''.join(date1)
print(date)

find = re.findall(r'ерез [0-9]+|В [0-9:-]+|в [0-9:-]+|ерез час', message)
find1 = ''.join(find)
print(find1)

day1 = re.findall(r'завтра|в понедельник|понедельник|во вторник|вторник|в среду|среду|в четверг|четверг|в пятницу|пятницу|в субботу|субботу|в воскресенье|воскресенье', message)
day = ''.join(day1)
print(day)

time1 = re.findall(r'в [0-9]?[0-9][./:;-][0-9][0-9]|в [0-9][0-9]', message)
print(time1)
time = ''.join(map(str,time1))
print(time)

clock = re.findall(r'минуты|часа|дня|минуту|часов|день|минут|час|дней', message)
clock1 = ''.join(clock)
print(clock1)

month = re.findall(r'\d\d?.(январ.|феврал.|март.|апрел.|ма.|июн.|июл.|август.|сентябр.|октябрь.|ноябр.|декабр.)', message)
month1 = ''.join(month)
print(month1)


print(text.replace(month1,''))




#format = "%d.%m.%Y"
#print("О чем мне вам напомнить?")
#message = input()
#text1 = re.findall(r"[^0-9.,;:-]", message)
#text = ''.join(text1)
#date1 = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9 ]', message)
#date = ''.join(date1)
#day1 = re.findall('завтра|(в понедельник)|(в? вторник)|в среду|в четверг|пятницу|субботу|воскресенье', message)
#day = ''.join(day1)


#time1 = re.findall('(в [0-9][0-9][./:;-][0-9][0-9])|(в [0-9][0-9])|(в [0-9][./:;-][0-9][0-9])', message)
#time = ''.join(time1)

#print(text,date1,day1,time1)

'''day = re.findall('завтра|понедельник|вторник|среду|четверг|пятницу|субботу|воскресенье', message)
day1 = ''.join(day)
datex = re.findall('[0-9][0-9][.,-][0-9][0-9][.,-][0-9][0-9][0-9][0-9 ]', message)
date_string = ''.join(datex)
dt2 = datetime.datetime.strptime(date_string, format)
print (text2)
print(date_string)
print(datetime.date.today())
print(dt2)'''