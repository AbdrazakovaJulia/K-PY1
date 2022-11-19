    import random
    import string

def get_random_password(n=8) -> str:
    var_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for _ in var_:
        rand = random.sample(var_, n)
    return "".join(rand)
print(get_random_password())
