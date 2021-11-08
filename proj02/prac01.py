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
    "tiger",
    "lion",
]

input("준비됬나요? 엔터를 누르면 시작합니다.")

random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0

for random_name in animal_names[0:5]:
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다")
    else:
        print("오타가 있어요.")

end_time = time.time()

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {end_time-begin_time}초 걸렸습니다.")
