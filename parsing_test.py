import re

with open("salrary","r") as f: lines=f.readlines()


i=0
salrary=0
sum_outlook=0
for line in lines:
    line=line.replace(",","")
    str_salrary=line.split("전망", 1)[0]
    outlook=line.split("전망", 1)[1]
    outlook=outlook.split("(", 1)[1]
    outlook=outlook.split("%", 1)[0]
    outlook=float(outlook)
    sum_outlook += outlook
#    print(outlook)
    str_salrary=re.findall(r'\d+',str_salrary)
#str_salrary=int(str_salrary[0])
    int_salrary=''.join(str_salrary)
#    print(int_salrary)
    int_salrary=int(int_salrary)
#    int_salrary=int(int_salrary)
    salrary = salrary + int_salrary
    i+=1
print("AVG of Salary :",salrary/i)
print("AVG of Outlook :",sum_outlook/i)
