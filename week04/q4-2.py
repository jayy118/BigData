import pandas as pd
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('file1.csv', encoding=('cp949'))
d1 = df #2013
df = pd.read_csv('file2.csv', encoding=('cp949'))
d2 = df #2023

d1.iloc[:, 0]

for i in range(0, d1.shape[0]):
    d1.iloc[i, 0] = d1.iloc[i, 0].split('(')[0].rstrip()
    
for i in range(0, d2.shape[0]):
    d2.iloc[i, 0] = d2.iloc[i, 0].split('(')[0].rstrip()

d1 = d1.iloc[:, :2]
d2 = d2.iloc[:, :2]

d3 = pd.concat([d1, d2], axis=1)
d3 = d3.iloc[:, [0, 1, 3]]
d3['2023년02월_총인구수'] = d3['2023년02월_총인구수'].str.replace(',', '').astype(float)
d3['2013년02월_총인구수'] = d3['2013년02월_총인구수'].str.replace(',', '').astype(float)
d3['인구 수 변화'] = d3.iloc[:, 2] - d3.iloc[:,1]

d3.plot.bar(x='행정구역', y='인구 수 변화', rot=90)
