from audioop import cross
from pprint import pp
import random
import matplotlib.pyplot as plt
# Import writer class from csv module
from csv import writer



def makePopulation(size, states):
    population = []
    for _ in range(size):
        chromosome = []

        for p, *neighbors in states:
            s = (p, random.choice(options), neighbors)
            chromosome.append(s)

        population.append(chromosome)

    return population


def findFitnessChromosome(chromosome):

    fitness = 0
    for gene in chromosome:
        for gene2 in chromosome:
            if gene[0] != gene2[0] and gene2[0] in gene[2] and gene[1] != gene2[1]:
                fitness += 1

    return fitness / 294


def findFitness(population):
    fitness10 = []

    for i in population:
        fitness10.append((i, findFitnessChromosome(i)))

    return fitness10


def makeTournaments(k, arr):
    parents10 = []

    for _ in range(int(len(arr) / k)):

        contestants = []
        for j in range(k):
            a = random.choice(arr)

            if a not in contestants:
                contestants.append(a)

        winner = contestants[0]

        for j in contestants:
            if j[1] > winner[1]:
                winner = j

        parents10.append(winner)

    return parents10


def crossover(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        a = random.choice([0, 1])
        if a == 0:
            arr3.append(arr1[i])
        else:
            arr3.append(arr2[i])

    return arr3


def crossover2(arr1, arr2):
    crossover_point = random.randrange(len(arr[1]))
    arr3 = arr1[:crossover_point] + arr2[crossover_point:]
    arr4 = arr2[:crossover_point] + arr1[crossover_point:]
    f3 = findFitnessChromosome(arr3)
    f4 = findFitnessChromosome(arr4)

    if f3 > f4:
        return arr3
    return arr4

def avg(arr):
    sum=0
    for i in arr:
        sum += i
    return sum/len(arr)

def makeKids(size, parents10):
    newPopulation = []

    while len(newPopulation) < size:

        parents = random.sample(parents10,2)

        newChromosome = crossover2(
            parents[0][0], parents[1][0]
        )
        newPopulation.append(newChromosome)

    return newPopulation


def mutate(arr, mutationRate, populationSize):
    
    mutatedGenes = int(len(arr[0]) * mutationRate * populationSize)
    indicesToMutate = random.choices([*range(64*populationSize)],k=mutatedGenes)
    for i in indicesToMutate:
        chromosome,gene = divmod(i,64)
        toAlter = list(arr[chromosome][gene])
        before = arr[chromosome][gene]
        toAlter[1] = random.choice([color for color in [*range(4)] if color != toAlter[1]])
        arr[chromosome][gene] = tuple(toAlter)
        after = arr[chromosome][gene]
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

    return (min, max, sum / len(arr))


def soln(arr, solved, numberofGenerations, size, tournamentSize, mutationRate):
    i = 1
    main10 = []

    fitness10 = [1, 2]
    parents10 = []

    main10 = makePopulation(size, arr)

    fitness10 = findFitness(main10)

    maxArray = []
    minArray = []
    avgArray = []


    while i < numberofGenerations and solved == False:

        parents10 = makeTournaments(tournamentSize, fitness10)

        chromosomeArr = makeKids(size, parents10)

        chromosomeArrFitness = mutate(chromosomeArr, mutationRate, size)
        fitness10 = findFitness(chromosomeArrFitness)

        t = findValues(fitness10)

        
         
        
        
        pp('#Generation '+ str(i))
        pp("Min is " + str(t[0]) + " Max is " + str(t[1]) + " Avg is " + str(t[2]))
        maxArray.append(t[1])
        minArray.append(t[0])
        avgArray.append(t[2])
        i += 1
         
        if int(t[1]) == 1:
            solved == True
            pp("done")
            length = list(range(1, i))
            plt.plot(length,maxArray, label="Max")
            plt.plot(length,minArray, label="Min")
            plt.plot(length,avgArray, label="Avg")

            plt.title("Graph")
            plt.xlabel("Generation")
            plt.ylabel("fitness val")
            # plt.annotate("Population size: "+ str(size) + " M: "+ str(mutationRate)+" # generations: "+str(numberofGeneration,xy = (5,5)))
            plt.show()
            break
    # pp("# generations: " +str(numberofGenerations) + " ;Population size " + str(size) + " ;Tournament size: "+ str(tournamentSize)+ " ;Mutation rate: " + str(mutationRate))
    # pp("Min is " + str(min(minArray))+ " Max is " + str(max(maxArray)) + " Avg is " + str(avg(avgArray)) + " in "+ str(i)+ " iterations")




if __name__ == "__main__":
    arr = []
    solved = False
    numberofGeneration = [50, 500, 5000]
    options = [0, 1, 2, 3]

    file = open("state_neighbors.txt", "r")
    for line in file:
        arr.append(line.split())
    
    mutationArray = [0.01,0.02,0.05,0.1]
    populationArr = [10,100,1000]
    generationSize = [50,500,5000]
    tournamentSize = [2,5,10]

    # for i in populationArr:
    #     for j in mutationArray:
    #         for k in generationSize:
    #             if(i == 10):
    #                 soln(arr,solved,k,i,2,j)
    #             else:
    #                 for m in tournamentSize:
    #                     soln(arr,solved,k,i,m,j)
    soln(arr, solved, 500, 100, 10,0.05)
