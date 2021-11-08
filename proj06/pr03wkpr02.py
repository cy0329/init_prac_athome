"""
과제 할때 참조할 것 (딕셔너리에 키 : 값 저장시)
"""

# dict1 = {ch:aa for aa in list} 이런식으로?

"""
3과 5의 공배수의 합을 계산하는 방법 두가지
"""
acc = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        acc += i

print(acc)


num_list = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        num_list.append(i)

print(sum(num_list))
