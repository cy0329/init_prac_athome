import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

# 과제1. 멜론TOP100 리스트에서 "곡명" 단어수 출력
# 총 100줄 중에 한 줄 출력의 예 : Dynamite => 1
print('멜론TOP100 리스트에서 "곡명" 단어수 출력')
# map은 함수의 '리턴값'으로 구성된 목록을 반환할 Iterator(예 : list)를 반환

# 곡명과 단어수를 같이 리턴하는 방법?
def map_fn1(s):
    return s["title"], len(s["title"].split())


a = list(map(map_fn1, song_list))
print(a)
# for s in map(map_fn1, song_list):
#     print(s)
