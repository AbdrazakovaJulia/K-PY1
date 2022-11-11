def get_unique_list_numbers() -> list[int]:
    from random import randint
    random_int = [randint(-10, 10) for _ in range(-10, 10)]
    unique_ = list(set(random_int))
    return unique_ # TODO написать функцию для получения списка уникальных целых чисел

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers)) == len(set(list_unique_numbers))
