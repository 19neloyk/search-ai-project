# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class Node:
    def __init__(self, current_state, parent, action_to_curr, step_cost, path_cost):
        self.state = current_state
        self.parent = parent
        self.action_to_curr = action_to_curr
        self.step_cost = step_cost
        self.path_cost = path_cost

    def __hash__(self):
        return self.state.__hash__()


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 74].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.18].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    frontier = util.Stack()
    explored = set()
    start_node = Node(problem.getStartState(), None, None, 1, 1)
    frontier.push(start_node)
    while not frontier.isEmpty():
        curr = frontier.pop()
        explored.add(curr.state)
        if problem.isGoalState(curr.state):
            path = []
            while curr.action_to_curr:
                path.append(curr.action_to_curr)
                curr = curr.parent
            print(len(path))
            return path[::-1]
        for successor, action, cost in problem.getSuccessors(curr.state):
            successor_node = Node(successor, curr, action, 1, curr.path_cost + 1)
            if successor not in explored:
                frontier.push(successor_node)



def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    "*** YOUR CODE HERE ***"
    frontier = util.Queue()
    explored = set()
    start_node = Node(problem.getStartState(), None, None, 1, 1)
    frontier.push(start_node)
    while not frontier.isEmpty():
        curr = frontier.pop()
        explored.add(curr.state)
        if problem.isGoalState(curr.state):
            path = []
            while curr.action_to_curr:
                path.append(curr.action_to_curr)
                curr = curr.parent
            print(len(path))
            return path[::-1]
        for successor, action, cost in problem.getSuccessors(curr.state):
            successor_node = Node(successor, curr, action, 1, curr.path_cost + 1)
            if successor not in explored:
                frontier.push(successor_node)


def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
