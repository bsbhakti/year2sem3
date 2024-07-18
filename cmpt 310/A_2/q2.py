# d1 = {'A':(1,2,3,4,5,6),
#     'B':(1,2,3,4,5,6),
#     'C':(1,2,3,4,5,6),
#     'D':(1,2,3,4,5,6),
#     'E':(1,2,3,4),
#     'F':(1,2,3,4),
# }
d1 ={
    'X':('t','f'),
    'Y':('t','f'),
    'Z':('t','f'),
}

                        
def isValid(node1,node2):
    if(node1.alphabet == 'X' & node2.alphabet == 'Y'):
       return( node1.value != node2.value)
    if(node1.alphabet == 'Y' & node2.alphabet == 'X'):
       return( node1.value != node2.value)
    if(node1.alphabet == 'Y' & node2.alphabet == 'Z'):
       return( node1.value != node2.value)
    if(node1.alphabet == 'Z' & node2.alphabet == 'Y'):
       return( node1.value != node2.value)
    return True




class Node:
  
    def __init__(self,alphabet,value, parent=None):
        """Create a search tree Node, derived from a parent by an action."""
        self.domain = d1[alphabet]
        self.parent = parent
        self.alphabet = alphabet
        self.value = value
        self.child1 
        self.child2
        self.child3
        self.child4
        self.child5
        self.child6
        
         
    def child_node(self,alphabet):
        # if(alphabet != 'E' & alphabet != 'F'):
            newNode1 =  Node(chr(ord(alphabet) + 1),1)
            newNode2 =  Node(chr(ord(alphabet) + 1),2)
            newNode3 =  Node(chr(ord(alphabet) + 1),3)
            newNode4 =  Node(chr(ord(alphabet) + 1),4)
            newNode5 =  Node(chr(ord(alphabet) + 1),5)
            newNode6 =  Node(chr(ord(alphabet) + 1),6)
             
            
            # stack.append(newNode5)
            # stack.append(newNode4)
            # stack.append(newNode3)
            # stack.append(newNode2)
            # stack.append(newNode1)

            if(isValid(self,newNode6)):
               self.child6 = newNode6
               stack.append(newNode6)
            if(isValid(self,newNode5)):
               self.child5 = newNode5
               stack.append(newNode5)
            if(isValid(self,newNode4)):
               self.child4 = newNode4
               stack.append(newNode4)
            if(isValid(self,newNode3)):
               self.child3 = newNode3
               stack.append(newNode3)
            if(isValid(self,newNode2)):
               self.child2 = newNode2
               stack.append(newNode2)
            if(isValid(self,newNode1)):
               self.child1 = newNode1
               stack.append(newNode1)

 
        # else:
            # newNode1 =  Node(1)
            # newNode2 =  Node(2)
            # newNode3 =  Node(3)
            # newNode4 =  Node(4)
            # # newNode5 =  Node(5)
            # # newNode6 =  Node(6)
            # self.child1 = newNode1
            # self.child2 = newNode2
            # self.child3 = newNode3
            # self.child4 = newNode4
            # self.child5 = newNode5
            # self.child6 = newNode6

    def expand(self):
        """List the nodes reachable in one step from this node."""
# def expand(self, problem):
#         """List the nodes reachable in one step from this node."""
#         return [self.child_node(problem, action)
#                 for action in problem.actions(self.state)]

#     def child_node(self, problem, action):
#         """[Figure 3.10]"""
#         next_state = problem.result(self.state, action)
#         next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
#         return next_node

    # def child_node(self, problem, action):
    #     """[Figure 3.10]"""
    #     action_desc = str(action) 
    #     next_state = problem.result(self.state, action)
    #     next_node = Node(next_state, self, action, action_desc, problem.path_cost(self.path_cost, self.state, action, next_state))
    #     return next_node

    def steps(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))


    # We want for a queue of nodes in breadth_first_graph_search or
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


# ______________________________________________________________________________

print(chr(ord("A") + 1))
stack = []

nodes = ['X',"Y"]
mynode = node('X','t')
stack.append()