import copy

Locations={"cs":0,"off":1,"Lab":2,"MR":3}

def main():
    solved=False
    horizon=0
    state= State()
    print("{} {} {} {} {}".format(state.RLoc, state.RHC, state.SWC, state.MW, state.RHM))
    while solved==False:
        solveCSP(state)
        # print(state.RLoc + " " + bool(state.RHC)+ " " + bool(state.SWC)+ " " + bool(state.MW)+ " " + bool(state.RHM))
        print("{} {} {} {} {}".format(state.RLoc, state.RHC, state.SWC, state.MW, state.RHM))
        print("\n\n\n")
        if(checkSolution(state)):
            solved=True
        else:
            horizon=horizon+1



def solveCSP(state):
    action=Action()
    goalState=currentGoalConstraint(state,action)

def checkSolution(state):
    return state.RLoc=="off" and state.SWC==False

def currentGoalConstraint(state,action):
    # Precondition for Delivering Coffee
    if(state.RHC==True and state.RLoc=="off"):
        action.DelC=True
        state.SWC=False
    # Precondition for Delivering Coffee
    elif(state.RLoc=="cs" and state.RHC!=True):
        action.PUC=True
        state.RHC=True
    # Precondition for delivering mail
    elif(state.RHM==True and state.RLoc=="off"):
        action.DelM=True
        state.RHM=False
    # Precondition for picking up mail
    elif(state.RLoc=="MR" and state.MW==True):
        action.PUM=True
        state.MW==False
    # Else we will need to Move
    else:
        if(state.RHC==True and state.RLoc!="off"):
            action.MOVE=True
            findNewStateAfterMove("off",state)
        elif(state.RHC==False and state.RLoc!="cs" and state.SWC==True):
            action.MOVE=True
            findNewStateAfterMove("cs",state)

def findNewStateAfterMove(targetLoc,state):
    isClockWiseResult=isClockWise(targetLoc,state.RLoc)
    setNewLocation(state,isClockWiseResult)
    
    
def isClockWise(targetLoc,startLoc):
    global Locations
    location=list(Locations.keys())
    movesClockwise=0
    startLocClockWise=startLoc
    movesCounterClockwise=0
    while(startLocClockWise!=targetLoc):
        if(startLocClockWise==location[len(Locations)-1]):
            startLocClockWise=location[0]
        else:
            startLocClockWise=location[Locations[startLocClockWise]+1]
        movesClockwise=movesClockwise+1

    while(startLoc!=targetLoc):
        if(startLoc==location[0]):
            startLoc=location[len(Locations)-1]
        else:
            startLoc=location[Locations[startLoc]-1]
        movesCounterClockwise=movesCounterClockwise+1

    if(movesClockwise<movesCounterClockwise):
        return True
    else:
        return False

def setNewLocation(state,isClockWise):
    global Locations
    location=list(Locations.keys())
    locationSource=Locations[state.RLoc]
    if(isClockWise):
        if(locationSource==len(Locations)-1):
            state.RLoc=location[0]
        else:
            locationSource=locationSource+1
            state.RLoc=location[locationSource]
    else:
        if(locationSource==0):
            state.RLoc=location[len(Locations)-1]
        else:
            locationSource=locationSource-1
            state.RLoc=location[locationSource]

class State:
  def __init__(self, RLoc="off", RHC=False,SWC=True,MW=False,RHM=True):
    self.RLoc = RLoc
    self.RHC = RHC
    self.SWC = SWC
    self.MW = MW
    self.RHM = RHM

class Action:
  def __init__(self, MOVE=False, PUC=False,DelC=False,PUM=False,DelM=False):
    self.MOVE=MOVE
    self.PUC=PUC
    self.DelC=DelC
    self.PUM=PUM
    self.DelM=DelM

if __name__ == "__main__":
    main()


"""
solved=false
horizon=0
while solved=false
    map strips into CSP with horizon
    solve CSP -> solution
    if(solution)
        solved=T 
    else
        horizon=horizon+1
return  solution
"""