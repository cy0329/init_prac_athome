"""
구구단
"""

# for num in range(2, 10):
#     print(f"<<< {num}단 >>>")
#     for i in range(1, 10):
#         print(f"{num}*{i} = {num*i}")

"""
구구단 함수
"""


def gugudan(num):
    print(f"### {num}단 ###")
    for x in range(1, 10):
        print(f"{num}*{x}={num*x}")


# for i in range(2, 10):
#     gugudan(i)

gugudan(int(input("몇단? : ")))
