my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

def calculate_average(list):
    sum = 0

    for i in list:
        sum += i

    average = sum / len(list)

    return average

print(calculate_average(my_list))
