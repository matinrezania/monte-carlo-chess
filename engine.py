class Engine():
    def __init__(self) -> None:
        pass

    def play(self, board):
        valid_input = False
        while not valid_input:
            move = input('move:')
            try:
                move = board.parse_san(move)
                valid_input = True
            except ValueError:
                print(f'{move} is not a valid move.')
                continue

        return move
