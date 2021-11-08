def calculate_sum(max_number):
    accmulator = 0
    for i in range(1, max_number + 1):
        accmulator += i
    return accmulator


print(calculate_sum(int(input("1부터 몇까지 더할까요? :"))))
