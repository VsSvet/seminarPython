def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in range(num_columns):
        print(*table[i])


if __name__ == '__main__':
    print_operation_table(lambda x, y: x * y)
