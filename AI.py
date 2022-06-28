import numpy as np
import copy
import random
from eval_funcs import *



def get_legal_moves(state):
    return list(state.legal_moves)


class MCTS_Node():
    def __init__(self, state, color, parent=None, parent_action=None):
        self.state = copy.deepcopy(state)
        self.color = color
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self.number_of_visits = 0
        self.score = 0
        self.untried_actions = get_legal_moves(self.state)



    def expand_tree(self):
        """
        Select a node to run the simulation
        It goes through the tree, It just goes until it finds a state that has no children or a state that the game is over.
        """
        current_node = self
        while not current_node.state.is_game_over():
            if current_node.untried_actions:
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node

    def expand(self):
        """
        Expands the current node with an untried action
        """
        random.shuffle(self.untried_actions)
        action = self.untried_actions.pop()

        next_state = copy.deepcopy(self.state)
        next_state.push(action)

        child_node = MCTS_Node(next_state, color=self.color,
                               parent=self, parent_action=action)
        self.children.append(child_node)

        return child_node


    def simulate(self):
        """
        From the current state simulate the game untill there is an outcome for the game
        """
        simulation_state = copy.deepcopy(self.state)

        while not simulation_state.is_game_over():

            possible_moves = get_legal_moves(simulation_state)

            action = self.select_random_move(possible_moves)
            simulation_state.push(action)


        out = simulation_state.outcome().result()
        if out == "1/2-1/2":
            return 0.5
        elif self.color == 'white' and out == "1-0" or self.color == 'black' and out == "0-1":
            return 1
        else:
            return 0


    def backpropagate(self, result):
        """
        Backpropagate the results
        """
        self.number_of_visits += 1.
        self.score += result
        if self.parent:
            self.parent.backpropagate(result)


    def best_child(self, c=5):
        """
        Select the best child
        """
        weights = []
        for child in self.children:
            res = total_evaluation(self.state)
            exploitation = 0
            if (self.color == "white"):
                exploitation = res['W']
            else:
                exploitation = res['B']
            exploitation += self.score / self.number_of_visits
            exploration = c * \
                np.sqrt((2 * np.log(self.number_of_visits) /
                        child.number_of_visits))
            ucb = exploration + exploitation
            #print(ucb*50)

            weights.append(ucb)

        return self.children[np.argmax(weights)]




    def select_random_move(self, possible_moves):
        """
        It selects the next move in the simulation step.
        """
        return possible_moves[np.random.randint(len(possible_moves))]


    def best_action(self, n_simulations, c):
        """
        Select the node corresponding to the best action
        """
        for i in range(n_simulations):
            expanded_tree = self.expand_tree()
            score = expanded_tree.simulate()
            expanded_tree.backpropagate(score)

        return self.best_child(c=c).parent_action
