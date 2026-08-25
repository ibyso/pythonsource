import pandas as pd

pd.set_option('display.max_colwidth', None)
# 기본읽기
df2 = pd.read_csv('./Bigpy/data/csv_s2.csv',sep=';')
print(df2)

# 0번째 행 스킵
# df = pd.read_csv('csv_s1.csv',skiprows=[0])
# print(df)

# print('-'*20)
# 0번째 행 스킵, header 생략
# df = pd.read_csv('csv_s1.csv',skiprows=[0],header=None)
# print(df)


# print('-'*20)
# df = pd.read_csv('csv_s1.csv',skiprows=[0],header=None, names=["Month",2023,2024,2025])
# print(df)

# print('-'*20)
# df = pd.read_csv('csv_s1.csv',skiprows=[0],header=None, names=["Month",2023,2024,2025], index_col=[0])
# print(df)


# 합계
df2['sum'] = df2[['Test1','Test2','Test2','Final']].sum(axis=1) #axis=1 행단위
print(df2)

# 평균
df2['avg'] = df2[['Test1','Test2','Test2','Final']].mean(axis=1)
print(df2)

# 저장
df2.to_csv("/Bigpy/data/result.csv",index=False)
print('저장완료')