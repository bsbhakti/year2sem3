from search import *
import time

def make_rand_StagePuzzle():
    mainTuple = (1,2,3,4,5,6,7,8,9,0)
    shuffledTuple = random.sample(mainTuple,len(mainTuple)) 
    # p = Problem(shuffledTuple)
    stageP = StagePuzzle(tuple(shuffledTuple))
    # stageP.initial = p.initial
    if(stageP.check_solvability(stageP.initial)==False):
        make_rand_StagePuzzle()
    # print(stageP.initial)
    return stageP



    
def display(state):
    j=1
    print(" ",end="")
    for a in state:
        if(a==0):
            print("*",end="")
        else:
            print(a,end="")

        if(j==2 or j==6 or j==10):
            print("")

        j=j+1

    print("")

# for i in range(8):

    # stage = make_rand_StagePuzzle()
    # t = time.time()
    # result = astar_search(stage, stage.h)
    # result1 = astar_search(stage, stage.ma_h)
    # result2 = astar_search(stage, stage.max_h)

    # print("Total run time with misplaced tiles: ",result[1])
    # print("Total run time with manhattan: ",result[1])
    # print("Total run time with misplaced tiles: ",result[1])
    # print(len(result[2]))
    # print(result[2])

    # s = time.time() - t

    # print(s)



list = [1,4,9,5,7,6,3,2,8,0]
stage = StagePuzzle(tuple(list))

# stage = make_rand_StagePuzzle()

display((stage.initial))



t = time.time()

result = astar_search(stage, stage.ma_h)
s = time.time() - t
print("Total run time with manhattan tiles: ", s)
print("Total number of nodes removed: ", result[1])
print("Solution length", len(result[2])-1)

t = time.time()
result = astar_search(stage, stage.h)
s = time.time() - t
print("Total run time with misplaced tiles: ", s)
print("Total number of nodes removed: ", (result[1]))
print("Solution length", len(result[2])-1)

t = time.time()
result = astar_search(stage, stage.max_h)
s = time.time() - t
print("Total run time with max tiles: ", s)
print("Total number of nodes removed: ", (result[1]))
print("Solution length", len(result[2])-1)