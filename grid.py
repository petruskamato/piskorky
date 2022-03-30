def create_array(rows,columns, symbol="_"):
    grid=[]
    for row in range(0,rows):
        temp_grid=[]
        for column in range (0,columns):
            temp_grid.append(symbol)
        grid.append(temp_grid)
    return grid

def print_grid(grid, rows, columns):
    print("   ", end="")
    for column in range (0, columns):
        print(column, end=" ")
    print()
    for row in range(0, rows):
        print(row, end="  ")
        for column in range (0, columns):
            print(grid[row][column],end=" ")
        print()

 