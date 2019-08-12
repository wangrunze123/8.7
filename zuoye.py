import csv
import re
path = 'C:/Users/戴尔/Desktop/un-general-debates'
with open(path,mode='r',encoding='utf-8')as f:
    csv_reader=csv.reader(f)
#priny(csv_reader)
    for row in csv_reader:
        q=row[3]
        path='C:/Users/戴尔/Desktop/wrz.txt'
    with open(path,'w',encoding='utf-8')as ro:
            ro.write(q)