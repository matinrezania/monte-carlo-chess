import chess.engine
from utils import *
import datetime
import chess
import time


def game():

    engine = Engine()

    game = GameSaver()
    game.headers['Event'] = 'Example'
    game.headers['Date'] = datetime.datetime.today().strftime(
        '%Y-%m-%d-%H:%M:%S')

    # if random.random() > 0.5:
    white = Player('white', engine)
    game.headers['White'] = 'Human'

    black = Player('black')
    game.headers['Black'] = 'MCTS'

    '''else:
        white = Player('white')
        game.headers['White'] = 'MCTS'
        black = Player('black', engine)
        game.headers['Black'] = engine.name'''

    board = chess.Board()

    white_turn = True

    print(f'{"Chess"}, MCTS param: c:, simul:')
    p1 = 'White'
    p2 = 'Black'
    print(f"{p1}: {game.headers['White']}, {p2}: {game.headers['Black']}")
    print()
    print('-- Initial State --')
    print(board, '\n\n')

    start = time.time()
    while not board.is_game_over():
        elapsed = time.time()
        if white_turn:
            move = white.play(board)
        else:
            move = black.play(board)
        elapsed = time.time() - elapsed

        print(
            f"{game.headers['White'] if white_turn else game.headers['Black']}'s move: {move}")
        print(
            f'Move computed in {datetime.timedelta(seconds=elapsed)} seconds')

        white_turn = not white_turn
        board.push(move)
        game.add_action(move, board, elapsed)

        print(board, '\n\n')
        print(f"{p1 if white_turn else p2}'s turn")

    game.headers["Result"] = board.result()

    if game.headers["Result"] == '1/2-1/2':
        print('Draw')
    else:
        print(f'The winner is {game.headers["Result"]}')

    engine.quit()

    seconds = time.time() - start
    print(f'C:{5}, - took {datetime.timedelta(seconds=seconds)}')


game()
