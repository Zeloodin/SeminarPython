from constant import cells_per_user

def gen_list():
    return ["" for i in range(cells_per_user)]

def gen_array(l = 1):
    return [gen_list() for i in range(l)]

