import pandas as pd
import openpyxl

# 첫번째 시트 읽어오기
# df = pd.read_excel("./Bigpy/data/excel_s1.xlsx",sheet_name=0,engine='openpyxl')
# print(df)
# print(df.head()) # 상위 5개
# print(df.tail()) # 하위 5개



# df = pd.read_excel("./Bigpy/data/excel_s1.xlsx",sheet_name=0,engine='openpyxl',skiprows=[1])
# print(df.head()) # 상위 5개



# df = pd.read_excel("./Bigpy/data/excel_s1.xlsx",sheet_name=0,engine='openpyxl',skiprows=[1], skipfooter=5)
# print(df.tail()) # 상위 5개


df = pd.read_excel("./Bigpy/data/excel_s1.xlsx",header=0)
# print(df.head()) # 상위 5개
print(list(df)) # 헤더만 리스트로 출력
print(list(df.columns.values))


# 전처리
# ^Unnamed : Unnamed로 시작하는 열
# na_values = '...' => null
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
print(df)

print('-'*20)

df = pd.read_excel("./Bigpy/data/excel_s1.xlsx",na_values=0,converters={"2019":lambda w: w if w> 60000 else None})
print(df)