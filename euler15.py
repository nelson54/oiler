grid_size = 20

ranges = list(reversed(range(0, grid_size)))
grid = [[0 for x in range(0, grid_size+1)] for y in range(0, grid_size+1)]

for b in range(0, grid_size):
    grid[b][grid_size] = 1
    grid[grid_size][b] = 1

for x in ranges:
    for y in ranges:
        grid[x][y] = grid[x+1][y] + grid[x][y+1]

print(grid[0][0])
