def is_valid(col, grid, num, row):

    if num in grid[row]:
        return False
    
    for i in range(9):
        if grid[i][col] == num:
            return False
        
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True 

def solver(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(col, grid, num, row):
                        grid[row][col] = num
                        if solver(grid):
                            return grid
                        grid[row][col] = 0
                return False
    return grid


def main():
    print('Enter the unsolved Sudoku grid (use 0 for empty cells):')
    unsolved_grid = []
    for _ in range(9):
        row = list(map(int, input().split()))
        unsolved_grid.append(row)

    solved_grid = solver(unsolved_grid)

    print('Solved Sudoku grid:')
    for row in solved_grid:
        print(' '.join(str(num) for num in row))

if __name__ == '__main__':
    main()

 
