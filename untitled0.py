import csv
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

f = open('file1.csv', encoding=('cp949'))
c = open('file2.csv', encoding=('cp949'))
data2 = csv.reader(f)
next(data2)
data1 = csv.reader(c)
next(data1)

x = []
result = []

for row1 in data1 :
    x.append(row1[0].split('(')[0].rstrip())
    for row2 in data2 :
        result.append(float(row1[1].replace(',', '')) - float(row2[1].replace(',', '')))
        break

print(result)
print(x)

plt.xticks(rotation=90)
plt.bar(x, result)
plt.savefig('result.png')