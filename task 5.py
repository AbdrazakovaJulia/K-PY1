def get_random_password() -> str:
    import string
    import random
    var_ = string.ascii_uppercase + string.ascii_lowercase + string.digits
    for _ in var_:
        rand = random.sample(var_, 8)
    return "".join(rand)
print(get_random_password())
