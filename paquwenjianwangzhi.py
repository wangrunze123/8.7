import csv
import re
file = 'C:/Users/戴尔/Desktop/access.log'
with open(file,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)  # 使用csv.reader读取csvfile中的文件
    file_ = 'C:/Users/戴尔/Desktop/网址.txt'
    asd = open(file_,'a',encoding='utf8')
    for row in csv_reader:  # 将csv 文件中的数据保存到birth_data中
        q = re.findall(r"\"http(.+?)\"",row[0])
        if q !=[]:
            qwe = 'http%s/'%q[0]
            asd.write('\n'+qwe)
    asd.close()