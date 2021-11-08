import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제6. 리스트에 랭크된 가수는 총 몇 팀? (중복 제거한 가수명 리스트의 크기)


def map_fn3(s):
    return s["artist"]


artists = set(map(map_fn3, song_list))
print("탑100에 랭크된 가수의 수 : ", len(artists))
