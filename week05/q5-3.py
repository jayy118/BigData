import csv
import pandas as pd

df = pd.read_csv('age.csv', encoding='cp949')

data = df

data

name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1 
result_name = '' 
areaname = ''
result = 0 
home = []  

for i in range(0, data.shape[0]-1) :
    if name in data.iloc[i, 0]:
        areaname=data.iloc[i, 0]
        for j in range(3, data.shape[1]-1): 
            home.append(data.iloc[i, j]) 
        hometotal=data.iloc[i, 2]

for k in range(len(home)):
    home[k]=(home[k]/hometotal) 

result_list=[]
away=[]


for i in range(0, data.shape[0]-1) :
    
    away=[]
    
    for j in range(3, data.shape[1]-1) :
        away.append(data.iloc[i, j])
        
    awaytotal=data.iloc[i, 2]
    
    for k in range(len(away)):

        away[k]=(away[k]/awaytotal)

    s=0

    for z in range(len(away)):

        s=s+(home[z]-away[z])**2

    result_list.append([data.iloc[i, 0], away, s])

result_list.sort(key=lambda s: s[2]) 



import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.figure(figsize = (10,5), dpi=300)            

plt.rc('font', family ='Malgun Gothic')

plt.title(name +' 지역과 가장 비슷한 인구 구조를 가진 지역(pandas)')

plt.plot(home, label = areaname)

plt.plot(result_list[1][1], label = result_list[1][0])

plt.plot(result_list[2][1], label = result_list[2][0])

plt.plot(result_list[3][1], label = result_list[3][0])

plt.plot(result_list[4][1], label = result_list[4][0])

plt.legend()

plt.show()