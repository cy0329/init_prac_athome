def get_max_index(number_list):
    number = number_list[0]
    max_index = 0
    for index, current_number in enumerate(
        number_list
    ):  # 리스트 내의 인덱스와 원소를 동시에 tuple 형태로반환 하는 것 enumerate
        if current_number > number:
            number = current_number
            max_index = index
    return max_index


numbers = [15, 67, 12, 2, 90, 84, 75]

print(get_max_index(numbers))
