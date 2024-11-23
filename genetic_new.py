import random

population_size = 10
chromosome_length = 6
target = '110110'
mutation_rate = 0.1
generations = 50

def gen_pop():
    population = []
    for i in range(population_size):
        chromosome = ''
        for j in range(chromosome_length):
            chromosome += random.choice('01')
        population.append(chromosome)
    return population

def fitness(chromosome):
    score = 0
    for i in range(chromosome_length):
        if chromosome[i] == target[i]:
            score += 1
    return score

def select_parents(population):
    scores = []
    for chromosome in population:
        scores.append(fitness(chromosome))
    parent1 = random.choices(population, weights=scores, k=1)[0]
    parent2 = random.choices(population, weights=scores, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(0, chromosome_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    mutated = ''
    for bit in chromosome:
        if random.random() < mutation_rate:
            mutated += random.choice('01')
        else:
            mutated += bit
    return mutated

def genetic_algorithm():
    population = gen_pop()
    for generation in range(1, generations + 1):
        best_chromosome = None
        best_fitness = -1
        for chromosome in population:
            current_fitness = fitness(chromosome)
            if current_fitness > best_fitness:
                best_fitness = current_fitness
                best_chromosome = chromosome
        print(f'Generation {generation} Best - {best_chromosome} Fitness = {best_fitness}')
        if best_chromosome == target:
            print('Target reached')
            break
        new_pop = []
        for i in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            new_pop.append(mutate(child1))
            new_pop.append(mutate(child2))
        population = new_pop

genetic_algorithm()
