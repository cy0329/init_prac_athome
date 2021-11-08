import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

print("멜론 TOP100 에서 곡 명 단어수 출력")

# 준수 버전
def make(song_dict):
    word = len((song_dict["title"]).split(" "))
    return word


def make_1(song_dict):
    title = song_dict["title"]
    return title


song_title_list = list(map(make_1, song_list))
song_word_list = list(map(make, song_list))


song_dic = dict(zip(song_title_list, song_word_list))
print(song_dic)
