list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

mux_num = max(list_numbers)
min_num = min(list_numbers)
maxindex = list_numbers.index(mux_num)
list_numbers[-1], list_numbers[maxindex] = list_numbers[maxindex], list_numbers[-1]
print(list_numbers)