population = list(map(int, input().split(', ')))
min_wealth = int(input())
poorest_population = [i for i in population if i < min_wealth]
highest_population = [i for i in population if i >= min_wealth]
needed_sum = 0
available_sum = 0
for i in range(len(poorest_population)):
    needed_sum += min_wealth - poorest_population[i]

for i in range(len(highest_population)):
    available_sum += highest_population[i] - min_wealth

if needed_sum > available_sum:
    print("No equal distribution possible")
elif needed_sum == available_sum:
    population = [min_wealth for i in population]
    print(population)
elif needed_sum < available_sum:
    for i in range(len(poorest_population)):
        max_highest = max(highest_population)
        index_max_highest = highest_population.index(max_highest)
        highest_population[index_max_highest] -= min_wealth - poorest_population[i]
        poorest_population[i] = min_wealth
    population = poorest_population + highest_population
    print(population)



