my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


new_list = []

for i in range(0, len(my_list)):
    if type(my_list[i]) == dict:
        new_list.append(my_list[i])
    elif type(my_list[i]) == list:
        new_list.append(my_list[i])


print(new_list)
