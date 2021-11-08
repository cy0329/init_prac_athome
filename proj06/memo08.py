import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제7. 2곡 이상 랭크된 가수는 몇 팀?

c = []
for i in song_list:
    c.append(i["artist"])

d = set(c)
for s in c:
    if c.count(s) < 2:
        d.remove(s)
print("2곡 이상 랭크된 가수 팀 수 :", len(d))
