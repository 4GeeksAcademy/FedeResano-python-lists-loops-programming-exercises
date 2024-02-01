list_of_numbers = [4, 80, 85, 59, 37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


def sort_odd_even(list):
    sorted_list = []
    even_list = []

    for i in list:
        if i % 2 != 0:
            sorted_list.append(i)
        else:
            even_list.append(i)

    for j in even_list:
        sorted_list.append(j)

    return sorted_list

print(sort_odd_even(list_of_numbers))

