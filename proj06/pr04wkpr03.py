"""
4일차 과제 다시해보기
"""

import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())


for i in song_list:
    if i["artist"] == "방탄소년단":
        print(i["title"])

print("=================")

for i in song_list:
    if "가을" in i["title"]:
        print(i["title"])

print("=================")

# acc = []
# for i in song_list:
#     if i["like"] > 200000:
#         acc.append(i["title"])
# print("좋아요가 20만이 넘는 곡수 : ", len(acc))

c1 = 0
for i in song_list:
    if i["like"] > 200000:
        c1 += 1
print("좋아요가 20만이 넘는 곡수 : ", c1)

print("=================")
# 1. 탑100 가수들만 전부 리스트화 (중복 있음)
# 2. 리스트화 된 가수들에서 중복 제거 > 집합(set) 사용하던지 다른 방법
# 3. 중복 있는 리스트와 없는 리스트를 비교 > 같은게 있을때마다 카운트 업
a = []  # 중복가수
b = []  # 가수
# 가수 리스트만 쭉 뽑음
for i in song_list:
    a.append(i["artist"])

# 중복 제거
# for a1 in a:
#     if a1 not in b:
#         b.append(a1)

b = set(a)

# 중복가수와 노중복 가수 비교
# for a2 in b:
#     count = 0
#     for a1 in a:
#         if a1 == a2:
#             count += 1
#     print(a2, "의 곡수 : ", count)

for a2 in b:
    c_s = a.count(a2)
    print(a2, "의 곡수 : ", c_s)
