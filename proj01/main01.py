import time

input("10초를 정확하게 맞혀라! 엔터를 누르면 시작!")
start = time.time()

input("10초를 정확히 세고 다시 엔터를 누르세요!")
end = time.time()

et = end - start
print("걸린 시간 : ", et, "초")
print("차이 : ", abs(et - 10), "초")
