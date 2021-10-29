"""
Update below functions with code to print different grids based on the input parameters.

NOTE: do not print anything besides the grid boxes in your functions.
"""


# PART 1
def create_edge_row():
    print('+ - - - - + - - - - +')


def create_filler_row():
    print('|         |         |')


def create_box():
    create_edge_row()
    create_filler_row()
    create_filler_row()
    create_filler_row()
    create_filler_row()


def print_grid1():
    create_box()
    create_box()
    create_edge_row()


# PART 2
def end_row():
    print('+')


def add_section(size):
    num_of_sec = size // 2
    print('+ ', end='')
    print(num_of_sec * '- ', end='')


def build_top_row(size):
    add_section(size)
    add_section(size)
    end_row()


def add_box_section(size):
    print('| ', end='')
    if size % 2 == 0:
        print(size * ' ', end='')
    else:
        print((size - 1) * ' ', end='')


def build_box_row(size):
    add_box_section(size)
    add_box_section(size)
    print('|')


def build_box(size):
    num_of_rows = size // 2
    for _ in range(num_of_rows):
        build_box_row(size)


def print_grid2(size):
    build_top_row(size)
    build_box(size)
    build_top_row(size)
    build_box(size)
    build_top_row(size)



# PART 3
def print_grid3(box_size, cell_size):
    pass


# executes your grid functions below
if __name__ == "__main__":
    # print_grid1()

    print_grid2(3)

    print_grid3(3, 4)
