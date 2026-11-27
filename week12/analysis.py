import pandas as pd
from pathlib import Path

df = pd.read_csv(Path(__file__).with_name("scores_2026.csv"))

def 정제(df):
	정제된_df = df.copy()

	# 점수가 비어 있는 행을 삭제한다.
	정제된_df = 정제된_df.dropna(subset=["점수"])
	print(f"결측 점수 삭제 후: {len(정제된_df)}행")

	# 모든 열의 값이 같은 중복 행을 삭제한다.
	정제된_df = 정제된_df.drop_duplicates()
	print(f"중복 행 삭제 후: {len(정제된_df)}행")

	# 반과 과목의 앞뒤 공백을 제거한다.
	정제된_df["반"] = 정제된_df["반"].str.strip()
	정제된_df["과목"] = 정제된_df["과목"].str.strip()
	print(f"공백 제거 후: {len(정제된_df)}행")

	# 점수가 0~100 범위를 벗어난 행을 삭제한다.
	정제된_df = 정제된_df[정제된_df["점수"].between(0, 100)]
	print(f"점수 범위 정리 후: {len(정제된_df)}행")

	return 정제된_df


정제된_df = 정제(df)

# 과목이 '수학'인 행만 남기기   
정제된_df = 정제된_df[정제된_df["과목"] == "수학"]
print(f"과목이 '수학'인 행 수: {len(정제된_df)}")


반별_점수_평균 = 정제된_df.groupby("반")["점수"].mean()
print("반별 점수 평균:")
print(반별_점수_평균)

# '과목'과 '반' 두 기준으로 묶기
과목_및_반_별_점수_평균 = 정제된_df.groupby(["과목", "반"])["점수"].mean()
print("과목 및 반별 점수 평균:")
print(과목_및_반_별_점수_평균)


반별_통계 = 정제된_df.groupby("반")["점수"].agg(["count", "mean", "median", "max"]).round(2)
print("반별 통계 (개수, 평균, 중앙값, 최댓값):")