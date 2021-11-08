import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제3. 좋아요 수가 가장 많은 곡은? 가장 적은 곡은?

print("<<좋아요 수가 가장 많은 곡>>")

# 기준값을 지정할 함수를 만들고
def max_fn1(s):
    return s["like"]


# max, min 과 함수만 조절하면 둘 다 가능

a = max(song_list, key=max_fn1)
print("제목 : ", a["title"])
print("좋아요 수 : ", a["like"])
print("참조 : ", a)
