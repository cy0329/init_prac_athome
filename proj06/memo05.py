import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제5. "곡명"의 글자수가 가장 많은 곡은? 가장 적은 곡은?
# 띄어쓰기 포함
def min_fn2(s):
    return len(s["title"])


c = min(song_list, key=min_fn2)
print("제목 : ", c["title"])
print("글자수 : ", len(c["title"]))
print("참조 : ", c, "\n")
