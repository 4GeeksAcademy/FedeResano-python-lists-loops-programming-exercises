parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

def get_parking_lot(matrix):
    parking = {"total_spots": 0, "available_spots": 0, "occupied_spots": 0}
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                parking["occupied_spots"] += 1
                parking["total_spots"] += 1
            elif matrix[i][j] == 2:
                parking["available_spots"] += 1
                parking["total_spots"] += 1

    return parking

get_parking_lot(parking_state)
