import random

x = random.randint(1, 100)

for i in range(10):
    print(f"남은 기회:{10-i}회")
    answer = input("1~100중에 숫자를 맞춰보세요. : ")
    a = int(answer)
    if i == 9:
        print("\n10회 끝 다음기회에..")
        break
    elif i < 9:
        if a > x:
            print("\n더 작은 수를 입력해주세요.")
        if a < x:
            print("\n더 큰 수를 입력해주세요.")
    else:
        print("정답!")
