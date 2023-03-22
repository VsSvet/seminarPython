# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
def check_input(arg1: str):
    return arg1.isdigit()


def convert_input(arg1: str):
    return int(arg1)


if __name__ == "__main__":
    count_el = input("Введите количество чисел в массиве: ")
    if check_input(count_el):
        count_el = convert_input(count_el)
        my_list = []
        for i in range(count_el):
            user_input = input("Введите элемент массива: ")
            if check_input(user_input):
                my_list.append(convert_input(user_input))
            else:
                my_list.append(0)

        number = input("Введите число которое необходимо найти в списке: ")
        if not check_input(number):
            print("Введите число")
        else:
            number = convert_input(number)
            min_diff = number - my_list[0]
            index_number = 0
            for i in range(1, count_el):
                count = number - my_list[i]
                if count < min_diff:
                    min_diff = count
                    index_number = i
            print(f"В массиве число {my_list[index_number]} самый близкий по величине элемент к числу {number}")
    else:
        print("Нужно ввести число.")
