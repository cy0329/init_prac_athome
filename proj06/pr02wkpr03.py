import random
import time

animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비됬으면 엔터!")

random.shuffle(animal_names)  # 방법1. 이미 사용된 random_name을 받았다면 다시 가져오는 것

begin_time = time.time()

ok_counter = 0

for count in range(5):
    random_name = random.choice(animal_names)
    print(random_name)
    line = input(">>> ")
    if line == random_name:
        ok_counter += 1
        print("정확!")
    else:
        print("오타!")

end_time = time.time()

print(f"{ok_counter}번 성공하였습니다.")
print(f"총 걸린 시간 : {end_time - begin_time}")
