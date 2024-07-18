from search import *

state = [[5, 2, 5, 2], [4, 4, 1, 1], [3, 3, 6, 6], [4, 4, 1, 1], [2, 5, 2, 5], [3, 3, 6, 6]]
 
# state = [[4, 4, 1, 1], [3, 6, 5, 5], [5, 5, 3, 6], [3, 6, 2, 2], [4, 1, 4, 1], [6, 3, 2, 2]]
# state = [
#     [   4, 4, 2, 2],[
#         1, 3, 5, 6],[
#         1, 1, 5, 5],[
#         6, 3, 6, 3],[
#         4, 2, 2, 4],[
#         3, 1, 6, 5]
# ]
goal_state = [[2,2,2,2],[6,6,6,6],[5,5,5,5],[3,3,3,3],[4,4,4,4],[1,1,1,1]]
mycube = Cube(state)

myNode = Node(state)
# myNode.expand(mycube)
astar_search(mycube,mycube.h_4)


# print(rotateBottomAntiClockwise(myNode.state))
# print((Rotate_Face_3_Anticlockwise(Rotate_Face_2_clockwisewise(Rotate_Face_5_Anticlockwise(myNode.state)))))

print()