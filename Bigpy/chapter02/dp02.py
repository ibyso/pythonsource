import pandas as pd
import numpy as np
import openpyxl

# 0~99 사이의 수를 100행 4열로 생성
df1 = pd.DataFrame(np.random.randint(0,100,size=(100,4)),columns=['ONE','TWO','THREE','FOUR'])
print(df1)

# 평균 0이고 표준편차 1인 정규분포 실수 생성 (10행 2열 컬럼명 AB)
df2 = pd.DataFrame(np.random.randn(10,2), columns=list('AB'))
print(df2)

df1.to_csv("./Bigpy/data/result2.csv",index=False)
df1.to_excel("./Bigpy/data/result2.xlsx",header=True,index=None)