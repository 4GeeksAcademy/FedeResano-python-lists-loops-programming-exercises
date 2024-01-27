my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]

def sum_odds():
    total = 0
    for i in range(0, len(my_list)):
        if my_list[i] % 2 != 0:
            total += my_list[i]

    return total

print(sum_odds())

