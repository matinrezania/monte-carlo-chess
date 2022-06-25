class Engine():
    def __init__(self) -> None:
        pass

    def play(self, board):
        good_value = False
        while not good_value:
            move = input('move:')
            try:
                move = board.parse_san(move)
                good_value = True
            except ValueError:
                print(f'{move} is not a valid move.')
                continue

        return move
