# welcome message
# ask for width and height of board


print("Welcome to Find Four!")
print("---------------------")
while True:
    height = int(input("Enter height of board (rows): "))
    if height > 25:
        print("Error: height can be at most 25!")
    elif height < 4:
        print("Error: height must be at least 4")
    else:
        break

while True:
    width = int(input("Enter width of borad (columns): "))
    if width > 25:
        print("Error: height can be at most 25!")
    elif width < 4:
        print("Error: height must be at least 4")
    else:
        break


def get_initial_board(rows: int, columns: int):
    board = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append('.')
        board.append(row)
    return board


def print_board(board: list[list[str]]):
    for row in board:  # for each row in the board
        for i in row:  # each space in the row
            print(row,
                  end='')  # print the corresponding list of strings withiut a space at the end so its all on one line
        print()  # one line of space after


# def insert_chip()
iBoard = get_initial_board(height, width)
print_board(iBoard)

