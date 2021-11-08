import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print('<<"곡명"의 단어수가 가장 많은 곡>>')


def max_fn2(s):
    return len(s["title"].split(" "))


c = max(song_list, key=max_fn2)
print("제목 : ", c["title"])
print("단어 수 : ", len(c["title"].split(" ")))
print("참조 : ", c)
