import utils as ut

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    all_data = '123456789'
    eliminate_dict = values.copy()

    for s in values:
        if values[s] == all_data:
            for p in ut.peers[s]:
                if len(values[p]) == 1:
                    eliminate_dict[s] = eliminate_dict[s].replace(
                        values[p], '')

    return eliminate_dict


sudoku_dict = ut.grid_values(grid)


print(eliminate(sudoku_dict))
