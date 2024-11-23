import random

population_size = 10
chromosome_length = 6
target = '110110'
mutation_rate = 0.1
generations = 50

def generate_pop():
    population = []
    for _ in range(population_size):
        chromosome = ''.join(random.choice('01') for _ in range(chromosome_length))
        population.append(chromosome)
    return population

def fitness(chromosome):
    score = 0
    for i in range(chromosome_length):
        if chromosome[i] == target[i]:  # Compare each bit with the target
            score += 1
    return score

def select_parents(population):
    scores = [fitness(chromosome) for chromosome in population]
    
    # Handle case where all scores are zero
    if sum(scores) == 0:
        scores = [1] * len(scores)
        
    parent1 = random.choices(population, weights=scores, k=1)[0]
    parent2 = random.choices(population, weights=scores, k=1)[0]
    return parent1, parent2

def crossover(parent1, parent2):
    point = random.randint(1, chromosome_length - 1)  # Ensure crossover happens within bounds
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def mutate(chromosome):
    mutated = ''.join(
        random.choice('01') if random.random() < mutation_rate else bit
        for bit in chromosome
    )
    return mutated

def genetic_algorithm():
    population = generate_pop()
    for generation in range(1, generations + 1):
        # Find the best chromosome in the population
        best_chromosome = max(population, key=fitness)
        best_fitness = fitness(best_chromosome)
        
        print(f"Generation {generation} Best - {best_chromosome} Fitness - {best_fitness}")
        
        # Stop if target is found
        if best_chromosome == target:
            print("Target Found!")
            break
        
        # Create the next generation
        new_population = []
        for _ in range(population_size // 2):
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        
        population = new_population  # Update the population with the new generation

genetic_algorithm()
