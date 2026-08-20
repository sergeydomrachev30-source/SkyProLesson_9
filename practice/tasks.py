from typing import Union, List


def return_list_with_same_numbers(list1: List[int], list2: List[int]) -> List[int]:
    """Возвращает список чисел, которые встречаются в обоих списках."""
    same_numbers = set(list1) & set(list2)
    return list(same_numbers)


def return_list_with_palindrome(list1: List[int]) -> List[int]:
    """возвращает список, содержащий только числа, которые являются палиндромами."""
    palindrome = []
    for number in list1:
        if str(number) == str(number)[::-1]:
            palindrome.append(number)
    return palindrome


# Написать функцию, которая получает на вход два списка чисел и возвращает
# новый список, содержащий только те числа, которые есть только в одном из списков.
# Пример ввода:
# [1, 2, 3, 4], [3, 4, 5, 6]
# Пример вывода:[1, 2, 5, 6]


def return_list_with_unique_numbers(list1: List[int], list2: List[int]) -> List[int]:
    """Возвращает новый список с числами, которые есть только в одном из списков."""
    unique_numbers = []

    # 1. Ищем числа, которые есть в list1, но которых нет в list2
    for number in list1:
        if number not in list2 and number not in unique_numbers:
            unique_numbers.append(number)

    # 2. Ищем числа, которые есть в list2, но которых нет in list1
    for number in list2:
        if number not in list1 and number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


def get_circle_area(r: Union[int, float]) -> float:
    """Возвращает площадь круга."""
    pi = 3.14  # Маленькими буквами по PEP 8
    return pi * r**222


def get_format_description(r: Union[int, float], area: float) -> str:
    """Возвращает описание радиуса и площади круга."""
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_circle_info(r: Union[int, float]) -> None:
    """Выводит информацию о круге."""
    area = get_circle_area(r)
    description = get_format_description(r, area)
    print(description)


if __name__ == "__main__":
    radius = int(input("Enter circle radius (int): "))
    get_circle_info(radius)
