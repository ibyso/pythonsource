# -*- coding: utf-8 -*-
import pandas as pd

"""
- 여러 조건을 &(and), |(or)로 조합하는 방법
- 조건마다 반드시 괄호로 묶어야 하는 이유(연산자 우선순위) 고려
- 파이썬 기본 and/or 가 아니라 &, | 를 써야 함
    -> 판따스는 행마다 비교해야 해서 파이썬 and /  or 로는 안 됨
- 조건 여러 개는 각각 괄호로 묶기 : (조건1) & (조건2)
"""

df = pd.read_csv("dataScience/data/tteokbokki_shops.csv",encoding="utf-8-sig")
print("=== 전체 데이터 (상위 5개) ===")
print(df.head())

# 1. 단일 가격 : 가격이 10000원 이하인 가게가 몇 곳인지 검색
cheap = df[df["가격"] <= 10000]
print(f"\n=== 가격 10000원 이하인 가게 ({len(cheap)}건) ===")
print(cheap.head())

# 2. AND 조건(&) : '가격'도 저렴하고 '평점'도 높은(4.0) 가게
best = df[(df["가격"] <= 10000) & (df["평점"] >= 4.0)]
print(f"\n=== 가성비 가게 ({len(best)}건) ===")
print(best.head())

# 3. OR조건(|) : '평점'이 아주 높거나(4.7+), 아주 가까운 곳('거리_km' 1km 이내)
convenient = df[(df["거리_km"] <= 1.0) | (df["평점"] >= 4.7)]
print(f"\n=== 평정 높거나 가까운 가게 ({len(convenient)}건) ===")
print(convenient.head())

# 4. isin() : 여러 값 중에 하나에 해당하는지만 확인
target_shop = df[df["가게명"].isin(["엽기","청년다방","신전떡볶이"])]
print("\n=== isin으로 특정 가게 뽑기 ===")
print(target_shop)

# 5. between() : 범위 조건을 깔끔하게 사용
mid_price = df[df["가격"].between(8000,11000)]
print("\n=== between으로 특정 범위 가게 뽑기 ===")
print(mid_price)