import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제7 map, filter 사용해서 해보기
print("\n<<2곡 이상 랭크된 가수는 몇 팀?>>")


def map_fn4(s):
    return s["artist"]


중복가수 = list(map(map_fn4, song_list))

가수 = set(중복가수)


def filter_fn2(s):
    return 중복가수.count(s) >= 2


두곡이상가수 = list(filter(filter_fn2, 가수))

print('2곡 이상 랭크된 가수 팀 수 : ', len(두곡이상가수))
