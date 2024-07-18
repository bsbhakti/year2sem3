
from audioop import cross
import random
import matplotlib.pyplot as plt


allpopulations =[[]]



# print(arr)

arr=[[]]

def makePopulation(size,arr):
    main10 = [[]]
    main10 = main10[1:]
    for i in range(size):
        temp = []
        # print("op")
        # print(i)
        for x in arr:
            # print("op1")
            # print(x)
            p = x[0]
            neighbors = x[1:]
            s = (p,random.choice(options),neighbors)
            # print("this is s")
            # print(s)
            temp.append(s)
        # print(arr)
        # print("this is temp")
        # print(temp)
        main10.append(temp)
    print("yoppopopo")
    # for i in main10:
    #     print((i))
    #     print("\n\n")
    return main10

def findFitnessChromosome(main10):
    fitness10 = [[]]
    fitness10 = fitness10[1:]
    # print("inside fitness-main")
    # print(main10)
    # for i in main10:
        # adj = 0
        # count10 =0
        # count = 0
        # print("this is i")
        # print(i)
    adj = 0
    count10 =0
    count = 0
            
    for j in main10: 
            # print("this is j in new crossover: ")
            # print(j)
         
            for k in main10:
                # print("this is k")
                # print(k)
                if(k[0] != j[0]):
                    count += 1
                    if(j[0] in k[2]):
                        # print("here")
                        # print(j[0])
                        adj += 1
                        if(j[1] != k[1]):
                            
                            count10+=1
            if(adj == 0):
                return
    # print("adj"+str(adj/2))
    # print("total count: " + str(count))
    toPut = adj/2
    count10 = count10/2
    fitness = count10/toPut
    return fitness

def findFitness(main10):
    fitness10 = [[]]
    fitness10 = fitness10[1:]
    # if(main10 not in allpopulations):
    #     allpopulations.append(main10)
    # else:

    #     print("already here")
        # print(main10[0])

    # print("inside fitness-main")
    # print(main10)
    for i in main10:
        adj = 0
        count10 =0
        count = 0
        # print("this is i")
        # print(i)
        for j in i:
            
            for k in i:
                # print("this is k")
                # print(k)
                if(k[0] != j[0]):
                    count += 1
                    if(j[0] in k[2]):
                        # print("here")
                        # print(j[0])
                        adj += 1
                        if(j[1] != k[1]):
                            
                            count10+=1
        if(adj == 0):
            return
        # print("adj"+str(adj/2))
        # print("total count: " + str(count))
        toPut = adj/2
        count10 = count10/2
        fitness = count10/toPut
        # print("fitness"+str(fitness))
        s = (i,fitness)
        fitness10.append(s)
    # print("this is fitness")
    # print(fitness10)
    return fitness10




def makeTournaments(k,arr):
    print("here in tournaments")
    print(arr)
    parents10 =[[]]
    parents10 = parents10[1:]
    start = 0
    maingroup =[]
    for i in range(int(len(arr)/k)):
        # print(arr[start])
        subgroup =[]
        for j in range(k):
            # group = arr[start:start+k]
            # start = start+k
            a = random.choice(arr)
            # print("this is the chosen one")
            # print(a)
            arr.remove(a)
            print(len(arr))
            if(a not in subgroup):
                subgroup.append(a)
        # print("tournament")
        # print(subgroup)
        # maingroup.append(subgroup)
        max = 0
        maxGroup =[]
        # maxGroup = maxGroup[1:]
        for j in subgroup:
            if j[1] > max:
                max = j[1]
                maxGroup = j
        parents10.append(maxGroup)            
    # print("parents")        
    # print((parents10))
    return parents10

def tournament(population, populationSize, k):
    numTournaments = populationSize//k
    parents = []
    for i in range(numTournaments):
        competitors = random.sample(population,numTournaments)
        max_fitness = 0
        for chromosome in competitors:
            # chrom_fit = calculateFitness(chromosome)
            if (chromosome[1]>max_fitness):
                max_fitness = chromosome[1]
                potential_winner = chromosome
        parents.append(potential_winner)
    return parents

def crossover(arr1,arr2):
    arr3 =[]
    for i in range(len(arr1)):
        a = random.choice([0,1])
        if(a ==0):
            arr3.append(arr1[i])
        else:
            arr3.append(arr2[i])
    # print("arr3: ")
    # print(len(arr3))
    return arr3

def crossover2(arr1,arr2):
    arr3 = arr1[:32] + arr2[32:]
    arr4 = arr2[:32] + arr1[32:]
    f3 = findFitnessChromosome(arr3)
    f4 = findFitnessChromosome(arr4)
    # print("arr3 fitness:")
    # print(f3)
    # print("arr4 fitness:")
    # print(f4)
    # print("arr3: ")
    # print(len(arr3))
    if(f3>f4):
        return arr3
    return((arr4))

def makeKids(size,parents10):
    # print("printing parents")
    # print(parents10)
    chromosomeArr =[[]]
    chromosomeArr = chromosomeArr[1:]
    newChromosome =[]
    # for i in range(size):
    while(len(chromosomeArr) < size):
        
        r1 = random.choice(parents10)
        r2 = random.choice(parents10)
        while(r1 == r2):
            r2 = random.choice(parents10)
            print("here")

        newChromosome = crossover2(r1[0],r2[0])    
    
        if(newChromosome not in chromosomeArr):
            chromosomeArr.append(newChromosome)

    print(chromosomeArr)
    print("printing chromosomeArr")
    
    return chromosomeArr


def mutate(arr, mutationRate, populationSize):
    mutatedGenes= len(arr[0]) * mutationRate * populationSize
    print(mutatedGenes)
    minColor = 0
    maxColor = 3
    
    # for j in arr:
               
            # for k in j:
                # print("pwwwee")
                # print(j)
    for i in range(int(mutatedGenes)):
                    randomChromosome = random.choice(arr)
                    indexOfRandomChromosome = arr.index(randomChromosome)
                    a = random.choice(randomChromosome)
                    # chromosome = j
                    # print("a before")
                    # print(a)
                    indexOfChoice = randomChromosome.index(a)
                    # print(indexOfChoice)
                    # print(j[indexOfChoice])
                    l = list(randomChromosome[indexOfChoice])
                    
                    l[1] = random.choice(options)

                    arr[indexOfRandomChromosome][indexOfChoice] = tuple(l)
                    # print("a after")
                    # print(j[indexOfChoice])
                    # print(j[0][indexOfChoice])
    # print("mutated")
    # print (arr)
    return arr

def findValues(arr):
    min = 64
    max = 0
    sum = 0
    for i in arr:
        if i[1] < min:
            min = i[1]
        if i[1] > max:
            max = i[1]
        sum += i[1]
        
    return (min,max,sum/len(arr))
        # for j in arr:


def soln(arr,solved,numberofGenerations,size,tournamentSize):
    i =0
    main10 = []
    

    # fitness10 = [[]]
    # fitness10 = fitness10[1:]
    cfitness10 = [[]]
    cfitness10 = cfitness10[1:]
    
    fitness10= [1,2]
    parents10 =[[]]
    parents10 = parents10[1:]
  
    # print("this is main before")
    # print(main10)
    main10 = makePopulation(size,arr)
    # print("this is main")

    # print(main10[1])
    fitness10 = findFitness(main10)
    # print("this is fitness outside")
    # fitness10 = fitness10[1:]
    # print(fitness10)
    print(len(fitness10))
    maxArray=[]
    minArray = []
    avgArray = []
    length = list(range(0, numberofGenerations))
    print(len(arr))
    while(i < numberofGenerations and solved == False):
     
        print("Number of iterationn helleeeeeo yes",str(i))
        # parents10 = makeTournaments(tournamentSize,fitness10)
        parents10 = tournament(fitness10,size,tournamentSize)
        # print("Parents len:"+str(len(parents10)))
        # print(parents10[0])
        # crossover(parents10[0][0],parents10[1][0])
        chromosomeArr = makeKids(size,parents10)
        # chromosomeArrFitness = findFitness(chromosomeArr)
        # print(len(chromosomeArrFitness))
        # print((chromosomeArrFitness))

        chromosomeArrFitness = mutate(chromosomeArr,0.01,size)
        fitness10 = findFitness(chromosomeArrFitness)
        # print(arr)
        
        t = findValues(fitness10)
        # print("Fitness of mutated")
        # print(fitness10)
        # print(len(fitness10))
        i+=1
        print("Min is "+str(t[0])+ "Max is "+str(t[1]) + "Avg is " + str(t[2]))
        maxArray.append(t[1])
        minArray.append(t[0])
        avgArray.append(t[2])
        if(int(t[1])== 1):
            solved == True
            print("done")
    

    plt.plot(length,maxArray,label ="Max")
    plt.plot(length,minArray,label ="Min")
    plt.plot(length,avgArray,label ="Avg")

    plt.title('Graph')
    plt.xlabel('generation')
    plt.ylabel('fitness val')
    plt.show()



arr = [[]]
arr = arr[1:]
# file = open("new.rtf","r")
file = open("state_neighbors.txt","r")

options = [0,1,2,3]

for x in file:
    # print("op1")
    k = (x.replace("\n",""))
    q = k.split(" ")
    # print(q)
    arr.append(q)
solved = False
# print(arr)
numberofGeneration = [50,500,5000]
# for i in numberofGeneration:
#     soln(arr,solved,i)
# print(arr)
# def soln(arr,solved,numberofGenerations,size,tournamentSize):
soln(arr,solved,50,100,2)