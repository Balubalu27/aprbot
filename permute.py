import argparse
import contextlib
import itertools


def args_parse():
    """Парсит аргументы командной строки"""
    parser = argparse.ArgumentParser(description='N')
    parser.add_argument('number_n', type=int, help='Input number N')
    args = parser.parse_args()
    return args.number_n


def conversion_to_the_list_of_nums(number_n):
    """
    Из полученного числа формирует список из чисел.
    Пример:
        number_n = 5,
        список на выходе [0, 0, 0, 0, 0, 1, 2, 3, 4, 5].

        number_n = 7,
        список на выходе [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7]
    """
    numbers_str = '0' * number_n + ''.join(str(i) for i in range(1, number_n + 1))
    numbers_list = [int(i) for i in numbers_str]
    return numbers_list


def get_uniq_combinations(number_list):
    """Возвращает множество из уникальных комбинаций"""
    numbers_set = set()
    for i in itertools.permutations(number_list):
        numbers_set.add(i)
    return numbers_set


def write_to_file(file_name, combinations_set):
    """Записывает уникальные значения set в файл через stdout"""
    with open(file_name, 'w') as file, contextlib.redirect_stdout(file):
        for j in combinations_set:
            print(j)


def main():
    try:
        n = args_parse()
        list_of_numbers = conversion_to_the_list_of_nums(n)
        uniq_combinations = get_uniq_combinations(list_of_numbers)
        write_to_file('number_log.txt', uniq_combinations)
        print('** Success permute.py **')

    except Exception as ex:
        print('Во время выполнения программы произошла ошибка:', ex)


if __name__ == '__main__':
    main()
