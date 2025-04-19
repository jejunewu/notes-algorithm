my_dict = {'b': 1, 'a': 3, 'c': 2}

# 按键排序
sorted_dict = {k: my_dict[k] for k in sorted(my_dict)}
print(sorted_dict)

# 按值排序
sorted_dict = dict(sorted(my_dict.items(), key=lambda x: x[1]))
print(sorted_dict)
