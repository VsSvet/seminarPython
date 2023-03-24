# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого
# множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
def check_input(arg1: str):
    return arg1.isdigit()


def get_set(number=" ", count_el=1):
    return set([input(f"Введите {i}й элемент {number} множества: ") for i in range(1, count_el + 1)])


if __name__ == "__main__":
    n, m, = input("Введите количество элементов множества 1: "), input("Введите количество элементов множества 2: ")
    if check_input(n) and check_input(m):
        count_el_set_1, count_el_set_2 = int(n), int(m)
        my_set_1, my_set_2 = get_set("первого", count_el_set_1), get_set("второго", count_el_set_2)
        result = sorted(my_set_1.intersection(my_set_2))
        print(f"Пересечения множеств: {', '.join(result)}") if result else print("Нет совпадающих элементов множеств")
    else:
        print("Нужно ввести число, а не строку")
