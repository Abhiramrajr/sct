import random
import numpy as np
from deap import base, creator, algorithms, tools

# Create custom fitness and individual types
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, -1.0))  # Minimize both distance and time
creator.create("Individual", list, fitness=creator.FitnessMulti)

# Define number of cities and their coordinates
num_cities = 10
city_coordinates = {i: (random.uniform(0, 100), random.uniform(0, 100)) for i in range(num_cities)}

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Evaluation function for TSP
def evaluate_tsp(individual):
    total_distance = sum(distance(individual[i], individual[i+1]) for i in range(len(individual) - 1))
    total_time = len(individual)  # For simplicity, consider the number of cities as time (steps)
    return total_distance, total_time

# Create toolbox and register functions
toolbox = base.Toolbox()
toolbox.register("indices", random.sample, range(num_cities), num_cities)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("mate", tools.cxOrdered)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.2)
toolbox.register("select", tools.selNSGA2)
toolbox.register("evaluate", evaluate_tsp)

# Main function
def main():
    population = toolbox.population(n=50)  # Initial population size
    ngen = 100  # Number of generations
    
    # Statistics: Compute average, minimum, and maximum fitness
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean, axis=0)
    stats.register("min", np.min, axis=0)
    stats.register("max", np.max, axis=0)
    
    # Run the genetic algorithm
    algorithms.eaMuPlusLambda(population, toolbox, mu=50, lambda_=100, cxpb=0.7, mutpb=0.2, ngen=ngen, stats=stats, halloffame=None, verbose=True)
    
    # Get and print the Pareto front (non-dominated individuals)
    pareto_front = tools.sortNondominated(population, len(population), first_front_only=True)[0]
    print("Pareto front: ")
    for ind in pareto_front:
        print(f"Objectives: {ind.fitness.values}, Tour: {ind}")

if __name__ == "__main__":
    main()
