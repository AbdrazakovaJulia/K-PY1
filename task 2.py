
def get_count_char(str_):
    import re
    spis = re.sub("[\n| !| .| ,]", "", main_str)
    lst = tuple(spis.lower())
    lst = [line.rstrip() for line in lst]
    dict = {symbol:lst.count(symbol) for symbol in lst}
    return dict
     # TODO посчитать количество каждой буквы в строке в аргументе str_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
