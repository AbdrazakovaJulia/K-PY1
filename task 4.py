import json


INPUT_FILE = "input.csv"

def csv_to_list_dict(INPUT_FILE, delimiter=',') -> list[dict]:
    listdict = []
    listrow = []
    with open(INPUT_FILE, 'r') as f:
        pop = f.readlines()
        zap = pop[0].rstrip().split(delimiter)
        for line in pop[1:]:
            listrow.append(line.rstrip().split(delimiter))
        for row in listrow:
            elem = {k: v for k, v in zip(zap, row)}
            listdict.append(elem)
    return  listdict
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
