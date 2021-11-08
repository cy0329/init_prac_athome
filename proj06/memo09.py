import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제8. '방탄소년단'의 좋아요 총 합은?
print("\n<<'방탄소년단'의 좋아요 총합은?>>")


def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


likes = []
for i in filter(filter_fn1, song_list):
    likes.append(i["like"])

print("방탄소년단 노래의 좋아요 총합 : ", sum(likes))
