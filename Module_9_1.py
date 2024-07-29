def apply_all_func(int_list, *functions):
    reuslts = {}
    for function in functions:
        key = function(int_list)
        reuslts.setdefault(function.__name__, key)
    return reuslts


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))