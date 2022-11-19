from random import randint

def get_unique_list_numbers(start=-10, stop=10, n=15) -> list[int]:
    random_int = []
    while len(random_int) < n:
        i = randint(start, stop)
        if i not in random_int:
            random_int.append(i)
    return random_int

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers)) == len(set(list_unique_numbers))
