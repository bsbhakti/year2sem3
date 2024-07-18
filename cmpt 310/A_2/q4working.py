from audioop import cross
from pprint import pp
import random
import matplotlib.pyplot as plt


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
    arr3 = arr1[:32] + arr2[32:]
    arr4 = arr2[:32] + arr1[32:]
    f3 = findFitnessChromosome(arr3)
    f4 = findFitnessChromosome(arr4)

    if f3 > f4:
        return arr3
    return arr4


def makeKids(size, parents10):
    print(parents10)
    print("printing parents")
    newPopulation = []

    while len(newPopulation) < size:

        parent_index1 = random.randint(0, len(parents10) - 1)
        parent_index2 = random.randint(0, len(parents10) - 1)

        if parent_index1 != parent_index2:
            newChromosome = crossover2(
                parents10[parent_index1][0], parents10[parent_index2][0]
            )
            newPopulation.append(newChromosome)

    return newPopulation


def mutate(arr, mutationRate, populationSize):
    mutatedGenes = len(arr[0]) * mutationRate * populationSize

    for _ in range(int(mutatedGenes)):
        randomChromosome = random.choice(arr)
        indexOfRandomChromosome = arr.index(randomChromosome)
        a = random.choice(randomChromosome)

        indexOfChoice = randomChromosome.index(a)

        l = list(randomChromosome[indexOfChoice])

        l[1] = random.choice(options)

        arr[indexOfRandomChromosome][indexOfChoice] = tuple(l)

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


def soln(arr, solved, numberofGenerations, size, tournamentSize):
    i = 0
    main10 = []

    fitness10 = [1, 2]
    parents10 = []

    main10 = makePopulation(size, arr)

    fitness10 = findFitness(main10)

    maxArray = []
    minArray = []
    avgArray = []
    length = list(range(0, numberofGenerations))

    while i < numberofGenerations and solved == False:

        parents10 = makeTournaments(tournamentSize, fitness10)

        chromosomeArr = makeKids(size, parents10)

        chromosomeArrFitness = mutate(chromosomeArr, 0.01, size)
        fitness10 = findFitness(chromosomeArrFitness)

        t = findValues(fitness10)

        i += 1
        pp('#Generation '+ str(i))
        pp("Min is " + str(t[0]) + " Max is " + str(t[1]) + " Avg is " + str(t[2]))
        maxArray.append(t[1])
        minArray.append(t[0])
        avgArray.append(t[2])

        if int(t[1]) == 1:
            solved == True
            pp("done")

    plt.plot(length, maxArray, label="Max")
    plt.plot(length, minArray, label="Min")
    plt.plot(length, avgArray, label="Avg")

    plt.title("Graph")
    plt.xlabel("generation")
    plt.ylabel("fitness val")
    plt.show()


if __name__ == "__main__":
    arr = []
    solved = False
    numberofGeneration = [50, 500, 5000]
    options = [0, 1, 2, 3]

    file = open("state_neighbors.txt", "r")
    for line in file:
        arr.append(line.split())

    soln(arr, solved, 50, 100, 2)
