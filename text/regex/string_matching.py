# !/usr/bin/env python

# This code is based on "https://gist.github.com/wil3/1671fbde4c698565040a" gist.

import string
import re
import random
import operator as op
from math import ceil, floor
from pathlib import Path
from typing import List, Tuple

import numpy
from random import (
    random,
    choice,
    randint,
    seed,
)
from deap import algorithms
from deap import base
from deap import creator
from deap import tools

VALID_CHARS = list(string.printable)
MAX_LENGTH = 100

MATE_RATIO = 0.6
MUTATION_RATIO = 0.9
POPULATION_SIZE = 50
MAX_GENERATIONS = 10e6
PATTERN = re.compile(r'\w{8}')


def get_random_char() -> chr:
    return choice(VALID_CHARS)


def gen_word(minimum: int, maximum: int) -> List[chr]:
    length = randint(minimum, maximum)
    return [get_random_char() for _ in range(length)]


def evaluate(individual: List[chr]) -> Tuple[float]:
    if not re.fullmatch(PATTERN, ''.join(individual)):
        return float('inf'),
    return len(individual),


def mutate(individual: List[chr]) -> Tuple[List[chr]]:
    r = random()
    c = get_random_char()
    pos = randint(0, len(individual) - 1)
    if r < 1 / 3:
        individual.append(c)
    elif 1 / 3 <= r < 2 / 3:
        individual.pop(pos)
    else:
        individual[pos] = c
    return individual,


def mate(ind1: List[chr], ind2: List[chr]) -> Tuple[List[chr], ...]:
    for i in range(min(len(ind1), len(ind2))):
        if random() < MATE_RATIO:
            ind1[i], ind2[i] = ind2[i], ind1[i]
    return ind1, ind2


def build() -> base.Toolbox:
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    # Attribute generator
    toolbox.register("attr_item", get_random_char)
    toolbox.register("attr_len", randint, 0, MAX_LENGTH)

    toolbox.register("word", gen_word, 1, MAX_LENGTH)
    # Structure initializers
    # toolbox.register("individual", init_individual)
    # toolbox.register("individual",tools.initRepeat, creator.Individual,
    #                 toolbox.attr_item, toolbox.attr_len)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.word)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    # Operator registering
    toolbox.register("evaluate", evaluate)
    toolbox.register("mate", mate)
    toolbox.register("mutate", mutate)
    toolbox.register("select", tools.selBest)

    return toolbox


def execute(toolbox: base.Toolbox, cases: int = 100) -> List[str]:
    population = toolbox.population(n=POPULATION_SIZE)
    hall_of_fame = tools.ParetoFront()

    stats = tools.Statistics(lambda i: i.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max", "best"

    # Evaluate every individuals
    for individual in population:
        individual.fitness.values = toolbox.evaluate(individual)

    hall_of_fame.update(population)
    record = stats.compile(population)
    logbook.record(gen=0, evals=len(population), **record)
    print(logbook.stream)

    generated_cases = list
    last_fitness = float('inf')
    current_fitness = None
    generation_count = 1
    while generation_count <= MAX_GENERATIONS and (last_fitness != current_fitness or current_fitness == float('inf')):
        last_fitness = current_fitness

        # Select the next generation individuals
        offspring = toolbox.select(population, floor(POPULATION_SIZE * 0.9))

        # Clone the selected individuals
        offspring = list(toolbox.map(toolbox.clone, offspring))

        # Add new individuals from the population
        offspring += toolbox.population(n=POPULATION_SIZE - len(offspring))

        # Apply crossover and mutation on the offspring
        for child1, child2 in zip(offspring[::2], offspring[1::2]):
            if not random() < MATE_RATIO:
                continue
            toolbox.mate(child1, child2)
            del child1.fitness.values
            del child2.fitness.values

        for mutant in offspring:
            if not random() < MUTATION_RATIO:
                continue
            toolbox.mutate(mutant)
            del mutant.fitness.values

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [individual for individual in offspring if not individual.fitness.valid]
        for individual in offspring:
            individual.fitness.values = toolbox.evaluate(individual)

        generated_cases = tools.selBest(population, k=cases)
        current_fitness = sum(toolbox.map(op.itemgetter(0), toolbox.map(toolbox.evaluate, generated_cases)))
        best = choice(generated_cases)
        word = "".join(best)

        # Select the next generation population
        population = toolbox.select(population + offspring, POPULATION_SIZE)
        record = stats.compile(population)
        logbook.record(gen=generation_count, evals=len(invalid_ind), best=word, **record)
        print(logbook.stream)

        generation_count += 1

    return [''.join(case) for case in generated_cases]


def main() -> None:
    seed(56)

    toolbox = build()
    generated_cases = execute(toolbox, 100)
    print(generated_cases)


if __name__ == "__main__":
    main()
