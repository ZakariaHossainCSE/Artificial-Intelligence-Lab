import random

def create_individual(N):
    
    individual = list(range(N))
    random.shuffle(individual)
    return individual
def fitness(individual):
    N = len(individual)
    non_attacks = 0
    total_pairs = N * (N - 1) // 2
    for i in range(N):
        for j in range(i + 1, N):
            if abs(individual[i] - individual[j]) != abs(i - j):
                non_attacks += 1
    return non_attacks

def selection(population, fitnesses):
    
    i1, i2 = random.sample(range(len(population)), 2)
    return population[i1] if fitnesses[i1] > fitnesses[i2] else population[i2]

def crossover(parent1, parent2):
    N = len(parent1)
    a, b = sorted(random.sample(range(N), 2))
    child = [None]*N
    child[a:b] = parent1[a:b]
    
    for i in range(a, b):
        if parent2[i] not in child:
            pos = i
            while child[pos] is not None:
                pos = parent2.index(parent1[pos])
            child[pos] = parent2[i]

    for i in range(N):
        if child[i] is None:
            child[i] = parent2[i]

    return child

def mutate(individual):
    a, b = random.sample(range(len(individual)), 2)
    individual[a], individual[b] = individual[b], individual[a]

def genetic_algorithm(N, population_size=100, max_generations=1000):
    population = [create_individual(N) for _ in range(population_size)]
    best_solution = None
    best_fitness = -1
    total_pairs = N * (N - 1) // 2

    for generation in range(max_generations):
        fitnesses = [fitness(ind) for ind in population]
        max_fit = max(fitnesses)

        if max_fit == total_pairs:
            best_solution = population[fitnesses.index(max_fit)]
            break

        new_population = []
        for _ in range(population_size):
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)
            child = crossover(parent1, parent2)
            if random.random() < 0.1:
                mutate(child)
            new_population.append(child)

        population = new_population

    return best_solution

def print_board(solution):
    N = len(solution)
    for i in range(N):
        row = ['Q' if solution[i] == j else '.' for j in range(N)]
        print(" ".join(row))

if __name__ == "__main__":
    N = int(input("Enter number of queens: "))
    solution = genetic_algorithm(N)
    if solution:
        print(f"Solution found for {N}-Queens:")
        print_board(solution)
    else:
        print("No solution found.")
