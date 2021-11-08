import pandas as pd

df = pd.read_csv("https://bit.ly/3nsLDXy")
song_list = list(df.T.to_dict().values())

"""과제1. 멜론TOP100 리스트에서 "곡명" 단어수 출력"""
# 총 100줄 중에 한 줄 출력의 예 : Dynamite => 1
# map은 함수의 '리턴값'으로 구성된 목록을 반환할 Iterator(예 : list)를 반환
print('<<멜론TOP100 리스트에서 "곡명" 단어수 출력>>')

# 방법1. 곡명만 리턴 받는 함수 >> print에서 길이만 따로
def map_fn1(s):
    return s["title"]


for s in map(map_fn1, song_list):
    print(s, "=>", len(s.split()))

## 위 방법은 map을 사용 하지 않아도 이렇게 쉽게 가능
## for s in song_list:
##     print(s["title"], len(s["title"].split()))

# 방법2. 곡명과 단어수를 같이 리턴. 이렇게도 가능하구나!
# ※실행시 위, 아래 중 하나는 주석처리

# def map_fn1(s):
#     return s["title"], len(s["title"].split())

# for s in map(map_fn1, song_list):
#     print(s)


"""과제2. "곡명" 단어수로 TOP10 곡명 출력"""
# 단어수가 제일 큰 노래가 우선순위가 높다.
# sorted 를 사용

print('\n<<"곡명" 단어수로 TOP10 곡명 출력>>')


def map_fn2(s):
    return s["title"]


a = list(map(map_fn2, song_list))
# print(a)


def sort_fn2(a):
    return len(a.split())


sorted_song_list = list(sorted(a, reverse=True, key=sort_fn2))
# print(sorted_song_list)
for ch_l in sorted_song_list[:10]:
    print(ch_l)


"""과제3. 좋아요 수가 가장 많은 곡은? 가장 적은 곡은?"""
# 기준값을 지정할 함수를 만들고

print("\n<<좋아요 수가 가장 많은 곡>>")


def max_fn1(s):
    return s["like"]


b = max(song_list, key=max_fn1)
print("제목 : ", b["title"])
print("좋아요 수 : ", b["like"])


print("\n<<좋아요 수가 가장 적은 곡>>")


def min_fn1(s):
    return s["like"]


c = min(song_list, key=min_fn1)
print("제목 : ", c["title"])
print("좋아요 수 : ", c["like"])

"""과제4. "곡명"의 단어수가 가장 많은 곡은? 가장 적은 곡은?"""
print('\n<<"곡명"의 단어수가 가장 많은 곡>>')


def max_fn2(s):
    return len(s["title"].split(" "))


d = max(song_list, key=max_fn2)
print("제목 : ", d["title"])
print("단어 수 : ", len(d["title"].split(" ")))


print('\n<<"곡명"의 단어수가 가장 적은 곡>>')


def min_fn2(s):
    return len(s["title"].split(" "))


e = min(song_list, key=min_fn2)
print("제목 : ", e["title"])
print("단어 수 : ", len(e["title"].split(" ")))

"""과제5. "곡명"의 글자수가 가장 많은 곡은? 가장 적은 곡은?"""
# 띄어쓰기 포함
print('\n<<"곡명"의 글자수가 가장 많은 곡>>')


def max_fn3(s):
    return len(s["title"])


f = max(song_list, key=max_fn3)
print("제목 : ", f["title"])
print("글자수 : ", len(f["title"]))


print('\n<<"곡명"의 글자수가 가장 적은 곡>>')


def min_fn3(s):
    return len(s["title"])


g = min(song_list, key=min_fn3)
print("제목 : ", g["title"])
print("글자수 : ", len(g["title"]))


"""과제6. 리스트에 랭크된 가수는 총 몇 팀? (중복 제거한 가수명 리스트의 크기)"""
print("\n<<리스트에 랭크된 가수는 총 몇 팀?>>")


def map_fn3(s):
    return s["artist"]


artists = set(map(map_fn3, song_list))
print("탑100에 랭크된 가수의 수 : ", len(artists))


"""과제7. 2곡 이상 랭크된 가수는 몇 팀?"""
# 방법1. map과 filter를 안쓰고 단계 구조화 해볼 용도
# print("\n<<2곡 이상 랭크된 가수는 몇 팀?>>")
# 중복가수 = []
# for i in song_list:
#     중복가수.append(i["artist"])

# 가수 = set(중복가수)
# for s in 중복가수:
#     if 중복가수.count(s) < 2:
#         가수.remove(s)
# print("2곡 이상 랭크된 가수 팀 수 :", len(가수))


# 방법2. map과 filter를 사용해 다시 만들어본 것
print("\n<<2곡 이상 랭크된 가수는 몇 팀?>>")


def map_fn4(s):
    return s["artist"]


중복가수 = list(map(map_fn4, song_list))

가수 = set(중복가수)


def filter_fn2(s):
    return 중복가수.count(s) >= 2


두곡이상가수 = list(filter(filter_fn2, 가수))

print("2곡 이상 랭크된 가수 팀 수 : ", len(두곡이상가수))


"""과제8. '방탄소년단'의 좋아요 총 합은?"""
print("\n<<'방탄소년단'의 좋아요 총합은?>>")


def filter_fn1(song_dict):
    return song_dict["artist"] == "방탄소년단"


likes = []
for i in filter(filter_fn1, song_list):
    likes.append(i["like"])

print("방탄소년단 노래의 좋아요 총합 : ", sum(likes))
