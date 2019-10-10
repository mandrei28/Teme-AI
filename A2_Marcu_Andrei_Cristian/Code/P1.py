from search import Problem

class WaterJug(Problem):

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """

        self.goal = goal
        Problem.__init__(self, initial, goal)
        self.maxJug = (4, 3)

    def actions(self, state):

        new_results = []

        if state[0] == 0:
            new_results.insert(0,(self.maxJug[0], 0))
        if state[1] == 0:
            new_results.insert(0,(0, self.maxJug[1]))
        if state[0] == self.maxJug[0]:
            new_results.insert(0,(-self.maxJug[0], 0))
        if state[1] == self.maxJug[1]:
            new_results.insert(0,(0, -self.maxJug[1]))
        if state[0] != 0 and state[1] != self.maxJug[1]:
            move_ammt = min(state[0], self.maxJug[1] - state[1])
            new_results.insert(0,(-move_ammt, +move_ammt))
        if state[1] != 0 and state[0] != self.maxJug[0]:
            move_ammt = min(state[1], self.maxJug[0] - state[0])
            new_results.insert(0,(+move_ammt, -move_ammt))

        return new_results

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        new_state = list(state)

        new_state[0] += action[0]
        new_state[1] += action[1]

        return tuple(new_state)

