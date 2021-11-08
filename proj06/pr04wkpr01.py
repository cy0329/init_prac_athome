"""
1. 문자열을 인자로 받아, 단어수를 반환하는 함수를 작성.
"""


# def get_word_count(s):
#     for i in s:
#         i = s.split()
#     return len(i)


def get_word_count(s):
    return len(s.split(" "))


s = input("단어수를 셀 문장 : ")
print(get_word_count(s))


# def get_count(s):
#     count = 0
#     for ch in s:
#         if ch != " ":
#             count += 1
#     return count

acc = []


def get_count(s):
    for i in s:
        if i != " ":
            acc.append(i)
    return len(acc)


print(get_count(s))


def cut_th(x):
    return x // 1000 * 1000


print(cut_th(int(input("1000단위 절사하고 싶은 수 : "))))
