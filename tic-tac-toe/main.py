game_is_on = True

print('\nWelcome to Tic-Tac-Toe! \'X\' goes first.\n'.upper())

# PRINTS THE BOARD

for row in range(3):
    print('-' * 13)
    for col in range(3):
        print(f'|   ', end='')
        if col == 2:
            print('|')
    if row == 2:
        print('-' * 13)

# EMPTY VARIABLES (IT'S A LOT I KNOW)

placements = []
pawn_symbols = ['X', '0']
o_row = []
o_col = []
x_row = []
x_col = []
diagonal1 = [(0,0), (1,1), (2,2)]
diagonal2 = [(0,2), (1,1), (2,0)]
x_place = []
o_place = []

while game_is_on:

    # USER INPUT FOR PAWN PLACEMENTS

    row = int(input('Please enter a value for the row(0 to 2): '))
    col = int(input('Please enter a value for the column(0 to 2): '))

    # CHECKING IF THE PLACEMENT POSITION IS ALREADY OCCUPIED

    if (row, col) in placements:
        print('\nPlace already occupied! Please enter a new input.\n')

        row = int(input('Please enter a value for the row(0 to 2): '))
        col = int(input('Please enter a value for the column(0 to 2): '))

    # STORING THE PLACEMENTS IN A LIST AS A TUPLE

    placements.append((row,col))

    # PRINTING THE BOARD AGAIN WITH THE PAWN IN PLACE

    for r in range(3):
        print('-' * 13)
        for c in range(3):
            if (r,c) in placements:
                index = placements.index((r,c))
                pawn = pawn_symbols[index % 2]
                print(f'| {pawn} ', end='')

                if c == 2:
                    print('|')
            else:
                print(f'|   ', end='')

                if c == 2:
                    print('|')

        if r == 2:
            print('-' * 13)

    # ADDING THE PLACEMENTS TO ANOTHER LIST BASED ON THE PLAYER TURNS

    if isinstance(placements[len(placements) - 1], tuple):
        r, c = placements[len(placements) -1]
        index = placements.index((r,c))
        if index % 2:
            o_row.append(r)
            o_col.append(c)
            o_place.append((r, c))
        else:
            x_row.append(r)
            x_col.append(c)
            x_place.append((r, c))

    # WINNING LOGIC

    for arr in [o_col, o_row, x_col, x_col]:
        if len(arr) >= 3:
            if arr[0] == arr[1] == arr[2]:
                if arr == x_col or arr == x_row:
                    print('X has won!')
                    game_is_on = False
                else:
                    print('0 has won!')
                    game_is_on = False

    # DIAGONAL WINNING LOGIC

    if set(diagonal1).issubset(x_place) or set(diagonal2).issubset(x_place):
        print("X won!")
        game_is_on = False
    elif set(diagonal1).issubset(o_place) or set(diagonal2).issubset(o_place):
        print("O won!")
        game_is_on = False

    # TO CHECK IF IT'S A DRAW

    if len(placements) == 9:
        print("It's a draw!")
        break