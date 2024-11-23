import numpy as np

def objective_function(x):
    return -x**2+4*x-4

population_size = 50
generations = 50
mutation_rate = 0.1

population = np.random.uniform(-10,10, size=population_size)

for generation in range(generations):
    fitness = objective_function(population)
    indices = np.argsort(fitness)[::-1]
    selected_pop = population[indices[:population_size]]
    crossover_pop = np.random.choice(selected_pop,size=population_size)
    mutation_mask = np.random.rand(population_size) < mutation_rate
    mutation_pop = np.random.uniform(-1,1,size=population_size)
    crossover_pop[mutation_mask] += mutation_pop[mutation_mask]
    population = crossover_pop

best_individaul = np.argmax(objective_function(population))
best_x = population[best_individaul]

print(f"Optimal x : {best_x}")
print(f"Optimal f(x) : {objective_function(best_x)}")