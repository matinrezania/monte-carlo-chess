import chess.pgn
import copy

available_games = {
    'chess': 'chess',
}


class Game():
    def __init__(self) -> None:

        self.headers = chess.pgn.Headers()
        self.game = chess.pgn.Game()
        self.history = self.game

    def add_action(self, action, board, elapsed):
        if self.game:
            self.history = self.history.add_variation(action)
            self.history.comment = str(elapsed)
        else:
            self.history.append((action, copy.deepcopy(board), elapsed))
