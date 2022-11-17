    import string
    import random

def get_random_password() -> str:
    var_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for _ in var_:
        n = 8
        rand = random.sample(var_, n)
    return "".join(rand)
print(get_random_password())
