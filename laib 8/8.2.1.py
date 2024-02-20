def neighbor_average(values, row, column):
    num_rows = len(values)
    num_columns = len(values[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    total_neighbors = 0
    total_sum = 0

    for dr, dc in directions:
        new_row = row + dr
        new_column = column + dc

        if new_row > 0 and new_row < num_rows and new_column > 0 and new_column < num_columns:
            total_neighbors += 1
            total_sum += values[new_row][new_column]

    if total_neighbors > 0:
        average = total_sum / total_neighbors
        return average 

values = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row = 1
column = 2
result = neighbor_average(values, row, column)
print(f"La media dei vicini di ({row}, {column}) è: {result}")
