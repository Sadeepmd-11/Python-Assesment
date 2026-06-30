def merge_twodictionaries(dict_a, dict_b):
    x = dict_a.copy()  

    for key, value in dict_b.items():
        if key in x:
            x[key] += value
        else:
            x[key] = value

    return x


dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

result = merge_twodictionaries(dict_a, dict_b)

print("Merged Dictionary:", result)