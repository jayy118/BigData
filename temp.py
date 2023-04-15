# [질의 3-1]
import pandas as pd

df=pd.read_csv('emp.csv')
df
emp=df

# [질의 3-2]
emp

# [질의 3-3]
emp.ename
emp['ename']
emp['ename'][:]


emp.loc[:,'ename']
emp.loc[0:13, 'ename']


emp.iloc[:,1]
emp.iloc[0:13, 1]
emp.iloc[0:14, 1]


# [질의 3-4]
emp[['ename', 'sal']] # 리스트로 전달
emp.loc[:, ['ename', 'sal']]
emp.iloc[:, [1,5]]

# [질의 3-5]
emp['job'].drop_duplicates()


# [질의 3-6]
emp[emp['sal']<2000]


# [질의 3-7]
emp[:][emp['sal']>1000][emp['sal']<2000]


# [질의 3-8]
emp[emp['sal']>=1500][emp['job']=='SALESMAN']


# [질의 3-9]
emp[:][(emp['job']=='MANAGER') | (emp['job']=='CLERK')]


# [질의 3-10]
emp[(emp['job']!='MANAGER') & (emp['job']!='CLERK')]


# [질의 3-11]
emp[['ename','job']][emp['ename']=='BLAKE']


# [질의 3-12]
emp[['ename','job']][emp['ename'].str.contains('AR')]


# [질의 3-13]
emp[:][(emp['ename'].str.contains('AR'))&(emp['sal']>=2000)]


# [질의 3-14]
emp[[emp['ename'].sort_values()], :]


# [질의 3-15]
emp['sal'].sum()


# [질의 3-16]
emp[emp['job']=='SALESMAN']['sal'].sum()


# [질의 3-17]
emp['sal'].sum(), (emp['sal'].sum())//(emp['sal'].count()),emp['sal'].min(),emp['sal'].max()


# [질의 3-18]
emp['sal'].count()


# [질의 3-19]
emp.groupby(by='job', dropna=False).agg({'ename':'count','sal':'sum'})


# [질의 3-20]
emp.dropna(subset='comm')


# [질의 4-0]
import pandas as pd

df=pd.read_csv('emp.csv')
df
emp=df

emp

# [질의 4-1]
emp['age']=[30,40,50,30,40,50,30,40,50,30,40,50,30,40]


# [질의 4-2]
emp.append({'empno':9999, 'ename':'ALLEN', 'job':'SALESMAN'}, ignore_index=True)


# [질의 4-3]
emp.drop(emp['ename'] == 'ALLEN')


# [질의 4-4]
emp.drop('hiredate')


# [질의 4-5]
emp.loc[emp['ename']=='SCOTT', 'sal']=3000


# [질의 5-1]
emp.rename(columns={'sal':'oldsal'})


# [질의 5-2]
emp['oldsal'] = emp['sal']


# [질의 5-3]
emp.drop('oldsal', axis=1)
