def calc_sum(max_number):
    sum = 0
    for i in range(max_number + 1):
        sum += i
    return sum


print(calc_sum(10))
