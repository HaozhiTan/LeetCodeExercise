# based on code from: https://github.com/aimacode/aima-python

import random
import time
from statistics import stdev

SEED = 1
random.seed(SEED)

class NQueensProblem:
    """
    The problem of placing N queens on an NxN board with none attacking
    each other. A state is represented as an N-element array, where
    a value of r in the c-th entry means there is a queen at column c,
    row r.

    This class operates on complete state descriptions where all queens are
    on the board in each state (one in each column c). This is in contrast to
    the NQueensProblem implementation in aima-python, whose initial state has
    no queens on the board, and whose actions method generates all the valid
    positions to place a queen in the first free column.
    """

    def __init__(self, N=None, state=None):
        if N is None:
            N = len(state)
        if state is None:
            state = tuple(0 for _ in range(N))
        assert N == len(state)
        self.N = N
        self.initial = state

    def actions(self, state: tuple) -> list:
        """Return a list containing all the valid actions for `state`.

        For each column c, one action is generated for each free row r in c,
        describing moving the queen in c from her current row to row r.

        This method does not take conflicts into account. It returns all
        actions which transform the current state into a neighbouring state.
        The neighbours of the current state are all states in which the
        position of exactly one queen is different. For example:
        (0, 0, 0, 0) and (0, 0, 0, 2) are neighbours, but
        (0, 0, 0, 0) and (0, 0, 1, 1) are not.

        Node.expand calls `result` with each action returned by `actions`.
        """
        ######################
        ### Your code here ###
        ######################
        valid_actions = [state[:column] + tuple([row]) + state[column + 1:] for row in range(self.N) for column in range(self.N) if row != state[column]]
        return valid_actions

    def result(self, state: tuple, action) -> tuple:
        """Return the result of applying `action` to `state`.

        Move the queen in the column specified by `action` to the row specified by `action`.
        Node.expand calls `result` on each action returned by `actions`.
        """
        ######################
        ### Your code here ###
        ######################
        return action

    def goal_test(self, state):
        """Check if all columns filled, no conflicts."""
        return self.value(state) == 0

    def value(self, state):
        """Return 0 minus the number of conflicts in `state`."""
        return -self.num_conflicts(state)

    def num_conflicts(self, state):
        """Return the number of conflicts in `state`."""
        num_conflicts = 0
        for (col1, row1) in enumerate(state):
            for (col2, row2) in enumerate(state):
                if (col1, row1) != (col2, row2):
                    num_conflicts += self.conflict(row1, col1, row2, col2)
        return num_conflicts

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def random_state(self):
        """Return a new random n-queens state.

        Use this to implement hill_climbing_random_restart.
        """
        return tuple(random.choice(range(self.N)) for _ in range(self.N))


class Node:
    """
    A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node.
    Delegates problem specific functionality to self.problem.
    """

    def __init__(self, problem, state, parent=None, action=None):
        """Create a search tree Node, derived from a parent by an action."""
        self.problem = problem
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def __eq__(self, node):
        return self.state == node.state

    def value(self):
        return self.problem.value(self.state)

    def goal_test(self):
        return self.problem.goal_test(self.state)

    def expand(self):
        """List the nodes reachable from this node."""
        state = self.state
        problem = self.problem
        return [
            Node(
                state=problem.result(state, action),
                problem=problem,
                parent=self,
                action=action,
            )
            for action in problem.actions(state)
        ]

    def best_of(self, nodes):
        """Return the best Node from a list of Nodes, based on problem.value.

        Sorting the nodes is not the best for runtime or search performance,
        but it ensures that the result is deterministic for the purpose of
        this assignment.
        """
        return max(
            sorted(nodes),
            key=lambda node: node.value(),
        )


def hill_climbing(problem):
    """
    [Figure 4.2] in the textbook.
    From the initial node, keep choosing the neighbor with highest value,
    stopping when no neighbor is better.
    """
    current = Node(problem=problem, state=problem.initial)
    while True:
        if current.goal_test():
            break
        neighbours = current.expand()
        if not neighbours:
            break
        neighbour = current.best_of(neighbours)
        if neighbour.value() <= current.value():
            break
        current = neighbour
    return current.state


def hill_climbing_instrumented(problem, **kwargs):
    """
    Find the same solution as `hill_climbing`, and return a dictionary
    recording the number of nodes expanded, and whether the problem was
    solved.
    """
    ######################
    ### Your code here ###
    ######################
    expanded = 0
    solved = False
    current = Node(problem=problem, state=problem.initial)
    while True:
        if current.goal_test():
            solved = True
            break
        neighbours = current.expand()
        expanded += 1
        if not neighbours:
            break
        neighbour = current.best_of(neighbours)
        if neighbour.value() <= current.value():
            break
        current = neighbour
    return {
        "expanded": expanded,
        "solved": solved,
        "best_state": current.state,
    }


def hill_climbing_sideways(problem, max_sideways_moves, **kwargs):
    """
    When the search would terminate because the best neighbour doesn't
    have a higher value than the current state, continue the search if 
    the the best neighbour's value is equal to that of the current state.

    But don't do this more than `max_sideways_moves` times. Watch out for
    off by one errors, and don't forget to return early if the search finds
    a goal state.
    """
    ######################
    ### Your code here ###
    ######################
    expanded = 0
    solved = False
    sideways_moves = 0
    current = Node(problem=problem, state=problem.initial)
    while True:
        if current.goal_test():
            solved = True
            break
        neighbours = current.expand()
        expanded += 1
        if not neighbours:
            break
        neighbour = current.best_of(neighbours)
        if neighbour.value() < current.value():
            break
        elif neighbour.value() == current.value():
            if sideways_moves == max_sideways_moves:
                break
            sideways_moves += 1
        current = neighbour
    return {
        "expanded": expanded,
        "solved": solved,
        "best_state": current.state,
        "sideways_moves": sideways_moves,
    }


def hill_climbing_random_restart(problem, max_restarts, **kwargs):
    """
    When the search would terminate because the best neighbour doesn't
    have a higher value than the current state, generate a new state to
    continue the search from (using problem.random_state).

    But don't do this more than `max_restarts` times. Watch out for
    off by one errors, and don't forget to return early if the search finds
    a goal state.

    To get consistent results each time, call random.seed(YOUR_FAVOURITE_SEED)
    before calling this function.
    """
    ######################
    ### Your code here ###
    ######################
    expanded = 0
    solved = False
    restarts = 0
    current = Node(problem=problem, state=problem.initial)
    while True:
        if current.goal_test():
            solved = True
            break
        neighbours = current.expand()
        expanded += 1
        if not neighbours:
            break
        neighbour = current.best_of(neighbours)
        if neighbour.value() < current.value():
            break
        elif neighbour.value() == current.value():
            if restarts == max_restarts:
                break
            restarts += 1
            current = Node(problem=problem, state=problem.random_state())
        else:
            current = neighbour
    return {
        "expanded": expanded,
        "solved": solved,
        "best_state": current.state,
        "restarts": restarts,
    }


def expanded_nodes(algorithm=hill_climbing_instrumented, N=4, solved_times=1000, **kwargs):
    expanded_node = []
    count = 0
    while True:
        problem = NQueensProblem(N=N, state=tuple(random.choice(range(N)) for _ in range(N)))
        results = algorithm(problem, **kwargs)
        if results['solved']:
            count += 1
            expanded_node.append(results['expanded'])
            if count >= solved_times:
                break
    avg_nodes = sum(expanded_node) / len(expanded_node)
    std_nodes = stdev(expanded_node)
    return avg_nodes, std_nodes


def time_to_solve(algorithm=hill_climbing_instrumented, N=4, solved_times=1000, **kwargs):
    time_spent = []
    count = 0
    while True:
        start_time = time.time()
        problem = NQueensProblem(N=N, state=tuple(random.choice(range(N)) for _ in range(N)))
        results = algorithm(problem, **kwargs)
        end_time = time.time()
        if results['solved']:
            count += 1
            time_spent.append(end_time - start_time)
            if count >= solved_times:
                break
    avg_time_spend = sum(time_spent) / len(time_spent)
    std_time_spend = stdev(time_spent)
    return avg_time_spend, std_time_spend


def problem_solving(algorithm=hill_climbing_instrumented, N=4, number_times_to_run=1000, **kwargs):
    problem_solved = 0
    for _ in range(number_times_to_run):
        problem = NQueensProblem(N=N, state=tuple(random.choice(range(N)) for _ in range(N)))
        results = algorithm(problem, **kwargs)
        problem_solved += results['solved']
    solving_probability = problem_solved / number_times_to_run
    return solving_probability


def report_results(algorithm, N_range, **kwargs):
    for N in N_range:
        avg_nodes, std_nodes = expanded_nodes(algorithm=algorithm, N=N, **kwargs)
        print("Average {} of nodes +/- {} std dev for {} Queens Problem using {} algorithm".format(avg_nodes, std_nodes, N, algorithm.__name__))
        avg_time_spend, std_time_spend = time_to_solve(algorithm=algorithm, N=N, **kwargs)
        print("Average time {} to solve +/- {} std dev for {} Queens Problem using {} algorithm".format(avg_time_spend, std_time_spend, N, algorithm.__name__))
        solving_probability = problem_solving(algorithm=algorithm, N=N, **kwargs)
        print("Probability of {} solving for {} Queens Problem using {} algorithm".format(solving_probability, N, algorithm.__name__))


if __name__ == '__main__':
    # Run the N = 6, 7, 8 Queens Problem
    # hill_climbing_instrumented
    N_range = range(6, 9)
    solved_times = 1000
    number_times_to_run = 1000
    max_sideways_moves = 20
    max_restarts = 20
    report_results(hill_climbing_instrumented, N_range, solved_times=solved_times, number_times_to_run=number_times_to_run,
                   max_sideways_moves=max_sideways_moves, max_restarts=max_restarts)
    report_results(hill_climbing_sideways, N_range, solved_times=solved_times, number_times_to_run=number_times_to_run,
                   max_sideways_moves=max_sideways_moves, max_restarts=max_restarts)
    report_results(hill_climbing_random_restart, N_range, solved_times=solved_times, number_times_to_run=number_times_to_run,
                   max_sideways_moves=max_sideways_moves, max_restarts=max_restarts)
