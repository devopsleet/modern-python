from contents import recipes


def my_deepcopy(d: dict) -> dict:
    new_dict = {}
    for key  in d:
        new_dict.append(d['key'])
    return new_dict.copy()


recipes_copy = my_deepcopy(recipes)
print(recipes_copy)
