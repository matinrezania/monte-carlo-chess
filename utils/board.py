import chess
import numpy as np


class RunningGameError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Board():
    def __init__(self) -> None:
        self.board = None
        self.white_turn = True
        self.winner = None

    @property
    def legal_moves(self):
        pass

    def push(self, action: tuple):
        pass

    def result(self):
        if not self.is_game_over():
            raise RunningGameError("The game is still running")

        return self.winner if self.winner else '1/2-1/2'

    def is_game_over(self):
        pass

    def outcome(self):
        color = chess.WHITE if self.winner == 'X' else chess.BLACK if self.winner == 'O' else None
        return chess.Outcome(termination='win' if color else 'draw', winner=color)
