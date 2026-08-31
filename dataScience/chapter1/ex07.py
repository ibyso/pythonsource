# -*- coding: utf-8 -*-
import pandas as pd

"""

"""

df = pd.read_csv("dataScience/data/survey.csv",encoding="utf-8-sig")
print(f"=== 원본 설문 응답({len(df)}건) ===")
print(df)

# 1. duplicated() : 응답자 ID 기준으로 중복 여부 확인
print("\n=== 응답자 ID 기준으로 중복 여부 확인 ===")
print(df.duplicated(subset="응답자ID"))

# 2. 중복된 응답자ID만 골라서 출력
dup_rows = df[df.duplicated(subset="응답자ID",keep=False)]
print(f"\n=== 중복 응답자 전체 내역 ({len(dup_rows)}건) ===")
print(dup_rows.sort_values("응답자ID"))

# 3. drop_duplicates() : 중복 제거, 기본은 첫 번째 응답만 유지(keep="first")
dup_first = df.drop_duplicates(subset="응답자ID", keep="first")
print(f"\n=== keep='first' 결과 : ({len(df)}건 => {len(dup_first)}건) ===")
print(dup_first)

# 4. keep="last" : 가장 마지막 응답만 유지
dup_last = df.drop_duplicates(subset="응답자ID", keep="last")
print(f"\n=== keep='last' 결과 : ({len(df)}건 => {len(dup_last)}건) ===")
print(dup_last)


# 5. keep="False" : 중복된 데이터 전체를 삭제
dup_unique_only = df.drop_duplicates(subset="응답자ID", keep=False)
print(f"\n=== keep = False 결과 : ({len(df)}건 => {len(dup_unique_only)}건) ===")
print(dup_unique_only)