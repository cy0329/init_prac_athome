import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제2. "곡명" 단어수로 TOP10 곡명 출력
# 단어수가 제일 큰 노래가 우선순위가 높다.
# sorted 를 사용

print('"곡명" 단어수로 TOP10 곡명 출력')


def map_fn2(s):
    return s["title"].split()


a = list(map(map_fn2, song_list))
# print(a)


def sort_fn2(a):
    return len(a)


sorted_song_list = list(sorted(a, reverse=True, key=sort_fn2))
# print(sorted_song_list)
for sl in sorted_song_list[:10]:
    print(sl)
