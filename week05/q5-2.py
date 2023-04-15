import numpy as np

import csv

f = open('age.csv')

data = csv.reader(f)

next(data)

data = list(data)

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')

mn = 1 

result_name = '' 

result = 0 

home = []  



for row in data :

    if name in row[0]:

        areaname=row[0]

        for i in row[3:]: 

            home.append(int(i)) 

        hometotal=int(row[2])

for k in range(len(home)):

    home[k]=(home[k]/hometotal) # ➊


result_list=[]

for row in data : 

    away=[]

    for i in row[3:]:

        away.append(int(i)) 

    awaytotal=int(row[2])

    for k in range(len(away)):

        away[k]=(away[k]/awaytotal)

    s=0

    for j in range(len(away)):

        s=s+(home[j]-away[j])**2

    result_list.append([row[0], away, s])

result_list.sort(key=lambda s: s[2]) 



import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.figure(figsize = (10,5), dpi=300)            

plt.rc('font', family ='Malgun Gothic')

plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역')

plt.plot(home, label = areaname)

plt.plot(result_list[1][1], label = result_list[1][0])

plt.plot(result_list[2][1], label = result_list[2][0])

plt.plot(result_list[3][1], label = result_list[3][0])

plt.plot(result_list[4][1], label = result_list[4][0])

plt.legend()

plt.show()