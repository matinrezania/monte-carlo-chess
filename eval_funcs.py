def total_evaluation(board):
    winner = None
    matrixed_board = board_to_matrix(board)


    piece_numbers = get_pieces_numbers(matrixed_board)
    print(
        f"Pieces_numbers: White: {piece_numbers['W']}, Black: {piece_numbers['B']}")

    piece_values = get_piece_values(matrixed_board)
    print(
        f"Piece_values: White: {piece_values['W']}, Black: {piece_values['B']}")

    kings_endangered = get_kings_safety(board, matrixed_board)
    print(
        f"Kings endanger by number of pieces: White: {kings_endangered['W']}, Black: {kings_endangered['B']}")


    white_totoal_score = piece_numbers['W'] + \
        piece_values['W'] + kings_endangered['W']
    black_totoal_score = piece_numbers['B'] + \
        piece_values['B'] + kings_endangered['B']*10
    print(
        f"Total_scores: White: {white_totoal_score}, Black: {black_totoal_score}")


    if(white_totoal_score > black_totoal_score):
        winner = 'White'
    elif (black_totoal_score > white_totoal_score):
        winner = 'Black'
    else:
        winner = 'Draw'  # for Draw
    return winner



def board_to_matrix(board):  # type(board) == chess.Board()
    pgn = board.epd()
    matrix = []  # Final board
    pieces = pgn.split(" ", 1)[0]
    rows = pieces.split("/")
    for row in rows:
        m = []  # This is the row I make
        for thing in row:
            if thing.isdigit():
                for i in range(0, int(thing)):
                    m.append('.')
            else:
                m.append(thing)
        matrix.append(m)
    # print(matrix)
    return matrix



def get_pieces_numbers(matrix):
    white_numbers = 0
    black_numbers = 0
    for row in matrix:
        for cell in row:
            match cell:
                case 'P':
                    white_numbers += 1
                case 'N':
                    white_numbers += 1
                case 'B':
                    white_numbers += 1
                case 'R':
                    white_numbers += 1
                case 'Q':
                    white_numbers += 1
                case 'K':
                    white_numbers += 1
                case 'p':
                    black_numbers += 1
                case 'n':
                    black_numbers += 1
                case 'b':
                    black_numbers += 1
                case 'r':
                    black_numbers += 1
                case 'q':
                    black_numbers += 1
                case 'k':
                    black_numbers += 1
                case default:
                    pass
    return{'W': white_numbers, 'B': black_numbers}



def get_piece_values(matrix):
    white_value = 0
    black_value = 0
    for row in matrix:
        for cell in row:
            match cell:
                case 'P':
                    white_value += 1
                case 'N':
                    white_value += 2
                case 'B':
                    white_value += 3
                case 'R':
                    white_value += 4
                case 'Q':
                    white_value += 5
                case 'K':
                    white_value += 6
                case 'p':
                    black_value += 1
                case 'n':
                    black_value += 2
                case 'b':
                    black_value += 3
                case 'r':
                    black_value += 4
                case 'q':
                    black_value += 5
                case 'k':
                    black_value += 6
                case default:
                    pass
    return{'W': white_value, 'B': black_value}



def get_kings_safety(board, matrix):
    white_king_r = None
    white_king_c = None
    black_king_r = None
    black_king_c = None
    row_index = 0
    col_index = 0
    for row in matrix:
        row_index += 1
        col_index = 0
        for cell in row:
            col_index += 1
            if(matrix[row_index-1][col_index-1] == 'K'):
                #print('found White king at', row_index, col_index)
                white_king_r = row_index
                match col_index:
                    case 1:
                        white_king_c = 'a'
                    case 2:
                        white_king_c = 'b'
                    case 3:
                        white_king_c = 'c'
                    case 4:
                        white_king_c = 'd'
                    case 5:
                        white_king_c = 'e'
                    case 6:
                        white_king_c = 'f'
                    case 7:
                        white_king_c = 'g'
                    case 8:
                        white_king_c = 'h'
            elif(matrix[row_index-1][col_index-1] == 'k'):
                #print('found Black king at', row_index, col_index)
                black_king_r = row_index
                match col_index:
                    case 1:
                        black_king_c = 'a'
                    case 2:
                        black_king_c = 'b'
                    case 3:
                        black_king_c = 'c'
                    case 4:
                        black_king_c = 'd'
                    case 5:
                        black_king_c = 'e'
                    case 6:
                        black_king_c = 'f'
                    case 7:
                        black_king_c = 'g'
                    case 8:
                        black_king_c = 'h'

    legal_moves = list(board.legal_moves)

    white_king_endangered = 0
    black_king_endangered = 0
    for move in legal_moves:
        if(str(move)[2:] == white_king_c+str(white_king_r)):
            white_king_endangered += 1
        elif(str(move)[2:] == black_king_c+str(black_king_r)):
            black_king_endangered += 1

    return{'W': white_king_endangered, 'B': black_king_endangered}
