from collections import Counter
from operator import indexOf
from numpy import * 

from utils import *
from imports import *
from queue import PriorityQueue
import copy

# from utils import PriorityQueue

class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        self.h = h(state)
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)] ####changed from :for action in problem.actions(self.state)] 

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    

    # We want for a q of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)



def h(state):
    temp = []
    total = 0
    # print(node[0])
    for i in state:
        count=Counter(i)
        # for j in state[i]:
        temp.append(len(count))

    count2 = Counter(temp)
    # print(count2)


    total +=  (4 * count2[4]) + (2 * count2[3]) + count2[2]
    # print(count2[4])
    # print(total)
    return total
def h_for_cube(state):
    temp = []
    total = 0
    # print(node[0])
    for i in state:
        count=Counter(i)
        # for j in state[i]:
        temp.append(len(count))

    count2 = Counter(temp)
    # print(count2)


    total +=  (4 * count2[4]) + (2 * count2[3]) + count2[2]
    # print(count2[4])
    # print(total)
    return total


def rotateTopAntiClockwise(node): # 4,0 and 4,1 #facet 2
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state
    state[1][1] = temp [0][3]
    state[1][3] = temp [0][2]
    state[0][2] = temp [3][0]
    state[0][3] = temp [3][2]
    state[3][0] = temp [4][1]
    state[3][2] = temp [4][0]
    state[4][1] = temp [1][3]
    state[4][0] = temp [1][1]

    state[2][0] = temp [2][1]
    state[2][3] = temp [2][2]
    state[2][2] = temp [2][0]
    state[2][1] = temp [2][3]
    return node

def rotateTopClockwise(node):
    rotateTopAntiClockwise(node)
    rotateTopAntiClockwise(node)
    rotateTopAntiClockwise(node)
    return node


def rotateBottomAntiClockwise(node): # 4,2 and 4,3 #facet 5
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state

    state[3][3] = temp [0][1]
    state[3][1] = temp [0][0]
    state[0][0] = temp [1][2]
    state[0][1] = temp [1][0] 
    state[4][3] = temp [3][1] 
    state[4][2] = temp [3][3]
    state[1][0] = temp [4][2] 
    state[1][2] = temp [4][3] 

    state[5][1] = temp [5][3]
    state[5][2] = temp [5][0]
    state[5][3] = temp [5][2]
    state[5][0] = temp [5][1]
    # print(temp)
    return node

def rotateBottomClockwise(node):
    rotateBottomAntiClockwise(node)
    rotateBottomAntiClockwise(node)
    rotateBottomAntiClockwise(node)
    return node

def rotateRightClockwise(node): #2,1 and 2,3 #facet 3
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state

    state[0][1] = temp [2][1]
    state[0][3] = temp [2][3]
    state[2][1] = temp [4][1]
    state[2][3] = temp [4][3] 
    state[4][1] = temp [5][1]
    state[4][3] = temp [5][3] 
    state[5][1] = temp [0][1]
    state[5][3] = temp [0][3] 

    state[3][1] = temp [3][0]
    state[3][2] = temp [3][3]
    state[3][3] = temp [3][1]
    state[3][0] = temp [3][2]
    return node

def rotateRightAntiClockwise(node):
    rotateRightClockwise(node)
    rotateRightClockwise(node)
    rotateRightClockwise(node)
    return node

def rotateLeftAntiClockwise(node): # 2,0 and 2,2 facet 1
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state

    state[0][0] = temp [2][0]
    state[0][2] = temp [2][2]
    state[2][0] = temp [4][0]
    state[2][2] = temp [4][2]
    state[4][0] = temp [5][0]
    state[4][2] = temp [5][2]
    state[5][0] = temp [0][0]
    state[5][2] = temp [0][2]

    state[1][1] = temp [1][3]
    state[1][2] = temp [1][0]
    state[1][3] = temp [1][2]
    state[1][0] = temp [1][1]
    return node

def rotateLeftClockwise(node):
    rotateLeftAntiClockwise(node)
    rotateLeftAntiClockwise(node)
    rotateLeftAntiClockwise(node)
    return node


def facet0AntiClockwise(node): #2,1 and 2,0 #facet 0
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state

    state[1][0] = temp [5][3]
    state[1][1] = temp [5][2]
    state[2][0] = temp [1][0]
    state[2][1] = temp [1][1]
    state[3][0] = temp [2][0]
    state[3][1] = temp [2][1]
    state[5][2] = temp [3][1]
    state[5][3] = temp [3][0]

    state[0][1] = temp [0][3]
    state[0][2] = temp [0][0]
    state[0][3] = temp [0][2]
    state[0][0] = temp [0][1]
    return node

def facet0Clockwise(node):
    facet0AntiClockwise(node)
    facet0AntiClockwise(node)
    facet0AntiClockwise(node)
    return node


def facet4AntiClockwise(node): #2,2 and 2,3 facet 4
    tempNode = copy.deepcopy(node)
    state = node.state
    temp = tempNode.state

    state[2][2] = temp [3][2]
    state[2][3] = temp [3][3]
    state[1][2] = temp [2][2]
    state[1][3] = temp [2][3]
    state[3][2] = temp [5][1]
    state[3][3] = temp [5][0]
    state[5][1] = temp [1][2]
    state[5][0] = temp [1][3]

    state[4][0] = temp [4][1]
    state[4][3] = temp [4][2]
    state[4][2] = temp [4][0]
    state[4][1] = temp [4][3]
    return node

def facet4Clockwise(node):
    facet4AntiClockwise(node)
    facet4AntiClockwise(node)
    facet4AntiClockwise(node)
    return node

# print(goal_state)



goal_state = [[1,1,1,1],
[2,2,2,2],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]]
# print("Heres the h value for the goal state ", h(goal_state))

# goal_state = [[0,1,2,3],[10,11,12,13],[20,21,22,23],[30,31,32,33],[40,41,42,43],[50,51,52,53]]

def actions1(node,arr):
        temp1 = copy.deepcopy(node)
        temp2 = copy.deepcopy(node)
        temp3 = copy.deepcopy(node)
        temp4 = copy.deepcopy(node)
        temp5 = copy.deepcopy(node)
        temp6 = copy.deepcopy(node)
        temp7 = copy.deepcopy(node)
        temp8 = copy.deepcopy(node)
        temp9 = copy.deepcopy(node)
        temp10 = copy.deepcopy(node)
        temp11 = copy.deepcopy(node)
        temp12 = copy.deepcopy(node)

        temp1 = rotateBottomAntiClockwise(temp1)
        temp2 = facet4AntiClockwise(temp2)
        temp3 = rotateTopAntiClockwise(temp3)
        temp4 = rotateRightClockwise(temp4)
        temp5 = rotateLeftAntiClockwise(temp5)
        temp6 = facet0AntiClockwise(temp6)
        temp7 = rotateBottomClockwise(temp7)
        temp8 = facet4Clockwise(temp8)
        temp9 = rotateTopClockwise(temp9)
        temp10 = rotateRightAntiClockwise(temp10)
        temp11 = rotateLeftClockwise(temp11)
        temp12 = facet0Clockwise(temp12) 
     
        # print("heres thr node", temp1)
        temp1.h = h(temp1.state)
        temp1.parent = node
        node.child1 = temp1

        temp2.h = h(temp2.state)
        temp2.parent = node
        node.child2 = temp2

        temp3.h = h(temp3.state)
        temp3.parent = node
        node.child3= temp3
    

        temp4.h = h(temp4.state)
        temp4.parent = node
        node.child4 = temp4

        temp5.h = h(temp5.state)
        temp5.parent = node
        node.child5 = temp5

        temp6.h = h(temp6.state)
        temp6.parent = node
        node.child6 = temp6

        temp7.h = h(temp7.state)
        temp7.parent = node
        node.child7 = temp7

        temp8.h = h(temp8.state)
        temp8.parent = node
        node.child8 = temp8

        temp9.h = h(temp9.state)
        temp9.parent = node
        node.child9 = temp9

        temp10.h = h(temp10.state)
        temp10.parent = node
        node.child10 = temp10

        temp11.h = h(temp11.state)
        temp11.parent = node
        node.child11 = temp11

        temp12.h = h(temp12.state)
        temp12.parent = node
        node.child12 = temp12



def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    if(len(frontier)>100):
        print("the frontier is long")
    
    explored = set()
    count_frontier = 0
    while frontier:
        node = frontier.pop()
        count_frontier += 1
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node, count_frontier, node.path()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return  count_frontier,node.path()

def astar_search_from_search(problem, h=None, display=True):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h_for_cube or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)

def astar_search(node,q):
    # n = Node(node)
    if (h(node.state)==0):
        return 'Found'

    else:
        temp1 = copy.deepcopy(node)
        temp2 = copy.deepcopy(node)
        temp3 = copy.deepcopy(node)
        temp4 = copy.deepcopy(node)
        temp5 = copy.deepcopy(node)
        temp6 = copy.deepcopy(node)
        temp7 = copy.deepcopy(node)
        temp8 = copy.deepcopy(node)
        temp9 = copy.deepcopy(node)
        temp10 = copy.deepcopy(node)
        temp11 = copy.deepcopy(node)
        temp12 = copy.deepcopy(node)

        temp1 = rotateBottomAntiClockwise(temp1)
        temp2 = facet4AntiClockwise(temp2)
        temp3 = rotateTopAntiClockwise(temp3)
        temp4 = rotateRightClockwise(temp4)
        temp5 = rotateLeftAntiClockwise(temp5)
        temp6 = facet0AntiClockwise(temp6)
        temp7 = rotateBottomClockwise(temp7)
        temp8 = facet4Clockwise(temp8)
        temp9 = rotateTopClockwise(temp9)
        temp10 = rotateRightAntiClockwise(temp10)
        temp11 = rotateLeftClockwise(temp11)
        temp12 = facet0Clockwise(temp12) 
     
        # print("heres thr node", temp1)
        temp1.h = h(temp1.state)
        temp1.parent = node
        node.child1 = temp1

        temp2.h = h(temp2.state)
        temp2.parent = node
        node.child2 = temp2

        temp3.h = h(temp3.state)
        temp3.parent = node
        node.child3= temp3
    

        temp4.h = h(temp4.state)
        temp4.parent = node
        node.child4 = temp4

        temp5.h = h(temp5.state)
        temp5.parent = node
        node.child5 = temp5

        temp6.h = h(temp6.state)
        temp6.parent = node
        node.child6 = temp6

        temp7.h = h(temp7.state)
        temp7.parent = node
        node.child7 = temp7

        temp8.h = h(temp8.state)
        temp8.parent = node
        node.child8 = temp8

        temp9.h = h(temp9.state)
        temp9.parent = node
        node.child9 = temp9

        temp10.h = h(temp10.state)
        temp10.parent = node
        node.child10 = temp10

        temp11.h = h(temp11.state)
        temp11.parent = node
        node.child11 = temp11

        temp12.h = h(temp12.state)
        temp12.parent = node
        node.child12 = temp12

        print(len(temp1.path()), temp1.h)

        # print("actual",temp1.h + len(temp1.path()))
        # print(temp1.state)
        if(temp1.state not in q.queue):
            q.put((temp1.h + len(temp1.path()),temp1.state))
        # q.put((temp1.h,temp1))
        if(temp2.state not in q.queue):
            q.put((temp2.h +len(temp2.path()),temp2.state))
        if(temp3.state not in q.queue):
            q.put((temp3.h + len(temp3.path()),temp3.state))
        if(temp4.state not in q.queue):
            q.put((temp4.h + len(temp4.path()),temp4.state))
        if(temp5.state not in q.queue):
            q.put((temp5.h + len(temp5.path()), temp5.state))
        if(temp6.state not in q.queue):
            q.put((temp6.h+ len(temp6.path()), temp6.state))
        if(temp7.state not in q.queue):
            q.put((temp7.h+ len(temp7.path()), temp7.state))
        if(temp8.state not in q.queue):
            q.put((temp8.h+ len(temp8.path()), temp8.state))
        if(temp9.state not in q.queue):
            q.put((temp9.h+ len(temp9.path()), temp9.state))
        if(temp10.state not in q.queue):
            q.put((temp10.h+ len(temp10.path()), temp10.state))
        if(temp11.state not in q.queue):
            q.put((temp11.h+ len(temp11.path()), temp11.state))
        if(temp12.state not in q.queue):
            q.put((temp12.h+ len(temp12.path()), temp12.state))
        # print((q.q))
        minNode = q.get()
        
        print("heres the popped value", minNode[0])
        # for i in (q.q):
        #     print(i)
        #     print("H value: ", i[0])

        # print("q ", list(q.heap), len(q.heap))
        print(minNode)
        myNode = Node(minNode[1])
        # myNode.state = minNode(1)
        astar_search(myNode,q)
        

    return 0

# state = [
#     [   4, 4, 2, 2],[
#         1, 3, 5, 6],[
#         1, 1, 5, 5],[
#         6, 3, 6, 3],[
#         4, 2, 2, 4],[
#         3, 1, 6, 5]
# ]
state = [[2,2,2,2],
[1,1,1,1],[3,3,3,3],[4,4,4,4],[5,5,5,5],[6,6,6,6]]
print(state)

# rotate = rotateBottomAntiClockwise(state)
# astar_search(state)
# rotate1 = rotateBottomAntiClockwise(state)
# rotate = rotateBottomAntiClockwise(state)
# print(rotate)
n = Node(state)
# initial = state
q = PriorityQueue()
# stage = StagePuzzle(initial) 
# print("look",stage.initial)

# astar_search(n,q)
# //result = astar_search(stage, stage.ma_h)
# astar_search(stage, stage.h_4)
# print(n.state)
# print(n.h)


myNode = Node(goal_state,None,rotateBottomAntiClockwise)
print(myNode.state)
astar_search(myCube,h_4)