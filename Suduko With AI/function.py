import utils as ut

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


def grid_values(grid):
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(ut.boxes, grid))

sudoku_dict = grid_values(grid)

print(ut.display(sudoku_dict))