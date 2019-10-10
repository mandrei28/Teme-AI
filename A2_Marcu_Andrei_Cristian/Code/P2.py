from search import Problem
import math

class Puzzle15(Problem):

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 4 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 4:
            possible_actions.remove('UP')
        if index_blank_square % 4 == 3:
            possible_actions.remove('RIGHT')
        if index_blank_square > 11:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP':-4, 'DOWN':4, 'LEFT':-1, 'RIGHT':1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


class Puzzle15MisDist(Puzzle15):
    def h(self, node):
        misplaced = 0 # the number of misplaced tiles
        dist = 0 # the distance between the misplaced tiles

        for i in range(15):
            if node.state[i] != self.goal[i]:
                misplaced += 1
        for i in node.state:
            dist += math.fabs(node.state.index(i) - self.goal.index(i))

        total_heurst = dist + misplaced

        return total_heurst
    
        
class Puzzle15MisColRow(Puzzle15):
    def h(self, node):
        misplaced_row = 0 # number of misplaced tiles on rows
        misplaced_col = 0 # number of misplaced tiles on columns

        for i in range(15):
            if node.state[i] != self.goal[i]:

                if i % 4 == 0:
                    misplaced_col += 1
                if i % 4 == 1:
                    misplaced_col += 1
                if i % 4 == 2:
                    misplaced_col += 1
                if i % 4 == 3:
                    misplaced_col += 1

                if i // 4 == 0:
                    misplaced_row += 1
                if i // 4 == 1:
                    misplaced_row += 1
                if i // 4 == 2:
                    misplaced_row += 1
                if i // 4 == 3:
                    misplaced_row += 1

        total_heurst = misplaced_col + misplaced_row
        
        return total_heurst
