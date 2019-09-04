# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

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
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    
    from game import Directions
    North = Directions.NORTH
    South = Directions.SOUTH
    East = Directions.EAST
    West = Directions.WEST 
    
    pathDict = {}
    visited = set()
    #visited start
    visited.add(problem.getStartState())
    #initial successors
    successor = problem.getSuccessors(problem.getStartState())
    for initSucc in successor:
        pathDict[initSucc[0]] = [initSucc[1]]
    #loop
    while (1):
        #if fringe = null, return failure
        if (len(successor) == 0):
            print "Fringe is empty"
            return util.raiseNotDefined()
        #(v, path) = fringe.pop
        succLocation = successor[0][0]
        succDirection = successor[0][1]
        del successor[0]
        #if isGoal = true, return path
        if problem.isGoalState(succLocation):
            return pathDict[succLocation]
        #if visited = false
        if succLocation not in visited:
            #visited = true
            visited.add(succLocation)
            #L = expand(v,path)
            tempSuccList = problem.getSuccessors(succLocation)
            #Fringe <- L
            for succ in reversed(tempSuccList):
                successor.insert(0,succ)
                pathDict[succ[0]] = []
                pathDict[succ[0]].extend(pathDict[succLocation])
                pathDict[succ[0]].append(succ[1])

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    from game import Directions
    North = Directions.NORTH
    South = Directions.SOUTH
    East = Directions.EAST
    West = Directions.WEST 
    
    pathDict = {}
    visited = set()
    #visited start
    visited.add(problem.getStartState())
    #initial successors
    successor = problem.getSuccessors(problem.getStartState())
    for initSucc in successor:
        pathDict[initSucc[0]] = [initSucc[1]]
    #loop
    while (1):
        #if fringe = null, return failure
        if (len(successor) == 0):
            print "Fringe is empty"
            return util.raiseNotDefined()
        #(v, path) = fringe.pop
        succLocation = successor[0][0]
        succDirection = successor[0][1]
        del successor[0]
        #if isGoal = true, return path
        if problem.isGoalState(succLocation):
            return pathDict[succLocation]
        #if visited = false
        if succLocation not in visited:
            #visited = true
            visited.add(succLocation)
            #L = expand(v,path)
            tempSuccList = problem.getSuccessors(succLocation)
            #Fringe <- L
            for succ in tempSuccList:
                repeat = False
                for s in successor:
                    if (s[0] == succ[0]):
                        repeat = True
                if (repeat == False):
                    successor.append(succ)
                    pathDict[succ[0]] = []
                    pathDict[succ[0]].extend(pathDict[succLocation])
                    pathDict[succ[0]].append(succ[1])

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    from game import Directions
    North = Directions.NORTH
    South = Directions.SOUTH
    East = Directions.EAST
    West = Directions.WEST 
    
    path = []
    pathPQ = util.PriorityQueue()
    visited = set()
    #visited start
    visited.add(problem.getStartState())
    #initial successors
    successor = problem.getSuccessors(problem.getStartState())
    for initSucc in successor:
        pathPQ.push((initSucc[0],[initSucc[1]],initSucc[2]),initSucc[2])
    #loop
    while (1):
        #if fringe = empty, return failure
        if (pathPQ.isEmpty() == True):
            print "Fringe is empty"
            return util.raiseNotDefined()
        #(v, path) = fringe.pop
        coordDirec = pathPQ.pop()
        #if isGoal = true, return path
        if problem.isGoalState(coordDirec[0]):
            return coordDirec[1]
        #if visited = false
        if coordDirec[0] not in visited:
            #visited = true
            visited.add(coordDirec[0])
            #L = expand(v,path)
            tempSuccList = problem.getSuccessors(coordDirec[0])
            #Fringe <- L
            for succ in tempSuccList:
                path = []
                path.extend(coordDirec[1])
                path.append(succ[1])
                pathPQ.push((succ[0],path,coordDirec[2] + succ[2]),coordDirec[2] + succ[2])
        
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    from game import Directions
    North = Directions.NORTH
    South = Directions.SOUTH
    East = Directions.EAST
    West = Directions.WEST 
    
    path = []
    pathPQ = util.PriorityQueue()
    visited = set()
    #visited start
    visited.add(problem.getStartState())
    #initial successors
    successor = problem.getSuccessors(problem.getStartState())
    for initSucc in successor:
        pathPQ.push((initSucc[0],[initSucc[1]],initSucc[2]),initSucc[2]+heuristic(initSucc[0],problem))
    #loop
    while (1):
        #if fringe = empty, return failure
        if (pathPQ.isEmpty() == True):
            print "Fringe is empty"
            return util.raiseNotDefined()
        #(v, path) = fringe.pop
        coordDirec = pathPQ.pop()
        #if isGoal = true, return path
        if problem.isGoalState(coordDirec[0]):
            return coordDirec[1]
        #if visited = false
        if coordDirec[0] not in visited:
            #visited = true
            visited.add(coordDirec[0])
            #L = expand(v,path)
            tempSuccList = problem.getSuccessors(coordDirec[0])
            #Fringe <- L
            for succ in tempSuccList:
                path = []
                path.extend(coordDirec[1])
                path.append(succ[1])
                #        location and path            cost                          cost + h
                pathPQ.push((succ[0],path,coordDirec[2] + succ[2]),coordDirec[2] + succ[2] + heuristic(succ[0],problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
