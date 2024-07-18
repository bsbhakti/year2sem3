from copy import deepcopy

initial_states = {'Rloc0':'off', 'RHC0':False, 'SWC0': True, 'MW0':False,'RHM0':True}

actions = {}
frontier = []
 
class Node:
    def __init__(self, RHC= False, SWC= True, MW = False,RHM = True, RLoc = 'off',parent = None, action= None):
      self.RLoc = RLoc
      self.RHC = RHC
      self.SWC = SWC
      self.MW = MW
      self.RHM = RHM
      self.parent = parent
      self.numberOFChildren = 0

      self.mcc = None
      self.PUCActionChild = None
      self.mc= None
      self.DelCActionChild = None
      self.PUMActionChild= None
      self.DelMActionChild= None
      self.action = action
    
    def moveCW_AW(self):
        child1 = deepcopy(self)
        child2 = deepcopy(self)
        child1.action = "mc"
        child2.action = "mcc"
        if(self.RLoc == "cs"):
            
            
            child1.RLoc = "off"
            child2.RLoc = "mr"
            child1.parent = self
            child2.parent = self
            self.numberOFChildren += 2
            self.mc = child1
            self.mcc = child2

        
        if(self.RLoc == "off"):
            child1.RLoc = "lab"
            
            child2.RLoc = "cs"
            child1.parent = self
            child2.parent = self
            self.numberOFChildren += 2
            self.mc = child1
            self.mcc = child2
           
        
        if(self.RLoc == "mr"):
            child1.RLoc = "cs"
            child2.RLoc = "lab"
            child1.parent = self
            child2.parent = self
            self.numberOFChildren += 2
            self.mc = child1
            self.mcc = child2


        if(self.RLoc == "lab"):
            child1.RLoc = "mr"
            child2.RLoc = "off"
            child1.parent = self
            child2.parent = self
            self.numberOFChildren += 2
            self.mc = child1
            self.mcc = child2


        return child1,child2

    def setConstraints(self):
        mcChild, mccChild = self.moveCW_AW()
        self.mcc = Node()
        self.mc = Node()
        self.mcc = mccChild
        self.mc = mcChild
        frontier.append(mccChild)
        frontier.append(mcChild)
       
        if(self.RLoc == "cs"):
            child1 = deepcopy(self)
            child1.RHC = True
            child1.action = "PUC"
            child1.parent = self
            frontier.append(child1)
            self.numberOFChildren += 1
            self.PUCActionChild = child1



        if(self.RLoc == "off" and self.RHC == True):
            child1 = deepcopy(self)
            child1.RHC = False
            child1.SWC = False
            child1.action = "DelC"
            child1.parent = self
            frontier.append(child1)
            self.numberOFChildren += 1
            self.DelCActionChild = child1

        if(self.RLoc == "mr" and self.MW == True):
            child1 = deepcopy(self)
            child1.RHM = True
            child1.MW = False
            child1.action = "PUM"
            child1.parent = self
            frontier.append(child1)
            self.numberOFChildren += 1
            self.PUMActionChild = child1


        
        if(self.RLoc == "off" and self.RHM == True):
            child1 = deepcopy(self)
            child1.RHM = False
            child1.action = "DM"
            child1.parent = self
            frontier.append(child1)
            self.numberOFChildren += 1
            self.DelMActionChild = child1


        
    
    
    def checkGoal(self):

        if(self.RLoc == "off" and self.SWC == False):
            return True
        else:
            return False
    
    def  displayState(self):
        print(self.RLoc)
        print(self.SWC)
        print(self.MW)
        print(self.RHM)
        print(self.RHC)

    def displayStates(self):
        if(self.mcc != None):
            print("mcc child")
        
        if(self.PUCActionChild != None):
            print("PUC child")
            print(self.PUCActionChild.displayState())

        if(self.mc != None):
            print("mc child")
            print(self.mc.displayState())
        
        if(self.DelCActionChild != None):
            print("DelC child")
            print(self.DelCActionChild.displayState())
        
        if(self.PUMActionChild != None):
            print("PUM child")
            print(self.PUMActionChild.displayState())
        
        if(self.DelMActionChild != None):
            print("delM child")
            print(self.DelMActionChild.displayState())
    

    def checkChildrenGoal(self):
        if(self.PUCActionChild != None and self.PUCActionChild.checkGoal() == True):
            return True,self.PUCActionChild

        if(self.DelCActionChild != None and self.DelCActionChild.checkGoal() == True):
            return True,self.DelCActionChild

        if(self.DelMActionChild != None and self.DelMActionChild.checkGoal() == True):
            return True,self.DelMActionChild

        if(self.mc != None and self.mc.checkGoal() == True):
            return True,self.mc

        if(self.mcc != None and self.mcc.checkGoal() == True):
            return True,self.mcc

        if(self.PUMActionChild != None and self.PUMActionChild.checkGoal() == True):
            return True,self.mcc

        else:
            return False
        
# states = {'Rloc':'off', 'RHC':False, 'SWC': True, 'MW':False,'RHM':True, 'Move':False}
        
    def path(self):
        currentNode = Node()
        horizon = []
        currentNode = self
        pathList = []
        i = 4
        pathList.append(currentNode.action)
        di = {'Rloc4':currentNode.RLoc, 'RHC4':currentNode.RHC,'SWC4':currentNode.SWC,'MW4':currentNode.MW,'RHM4':currentNode.RHM}
        
        horizon.append(di)
        while(currentNode.parent.action != None):
            parent = Node()
            parent = currentNode.parent
            pathList.append(parent.action)
            i -= 1
            di = {f"Rloc{i}":parent.RLoc, f'RHC{i}':parent.RHC,f'SWC{i}':parent.SWC,f'MW{i}':parent.MW,f'RHM{i}':parent.RHM}
            horizon.append(di)
            currentNode = parent
        horizon.append(initial_states)
        return pathList,horizon

    

def main():
    initialNode = Node()
    solved = False
    while( solved == False ):
        initialNode.setConstraints()
        solved = initialNode.checkChildrenGoal()
        initialNode = frontier.pop(0)
    solvedNode = Node()
    boolean,solvedNode = solved
    path,directory = (solvedNode.path())
    displayCSP(path,directory)


def displayCSP(path,directory):
    path.reverse()
    print("Path found "+ str(path))
    directory.reverse()
    a = (addActions(path))
    
    print("Horizon "+str(len(directory)-1))
    if(directory != None):
        for i in directory:
            print("")
   
            for j in i:
                print(j + ": "+str(i[j]))
            if(directory.index(i) < len(directory)-1):
                displayActions(a,directory.index(i))
                print("")
          

def displayActions(d,index):
    print(f"Actions{index}")
    for i in d[index]:
        print(i + ": "+str(d[index][i]))

def addActions(path):
    l = []
    di2 = {}
    for i in path:
        if(i == 'mcc' or i =='mc'):
            di2 = {f"Move{ path.index(i)}":True, f"PUC{ path.index(i)}":False, f"DelC{ path.index(i)}":False, f"PUM{ path.index(i)}":False,f"DelM{ path.index(i)}":False}
        if(i =='PUC'):
            di2 = {f"Move{ path.index(i)}":False, f"PUC{ path.index(i)}":True, f"DelC{ path.index(i)}":False, f"PUM{ path.index(i)}":False,f"DelM{ path.index(i)}":False}
        if(i == 'DelC'):
            di2 = {f"Move{ path.index(i)}":False, f"PUC{ path.index(i)}":False, f"DelC{ path.index(i)}":True, f"PUM{ path.index(i)}":False,f"DelM{ path.index(i)}":False}
        if(i == 'PUM'):
            di2 = {f"Move{ path.index(i)}":False, f"PUC{ path.index(i)}":False, f"DelC{ path.index(i)}":False, f"PUM{ path.index(i)}":True,f"DelM{ path.index(i)}":False}
        if(i == 'DelM'):
            di2 = {f"Move{ path.index(i)}":False, f"PUC{ path.index(i)}":False, f"DelC{ path.index(i)}":False, f"PUM{ path.index(i)}":False,f"DelM{ path.index(i)}":True}
        l.append(di2)
    return l






main()



