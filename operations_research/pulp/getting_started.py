from pulp import (
    LpVariable,
    LpProblem,
    LpMinimize,
    LpStatus,
)


def main():
    x = LpVariable("x", 0, 3)
    y = LpVariable("y", 0, 1)

    problem = LpProblem("myProblem", LpMinimize)
    problem += x + y <= 2
    problem += -4 * x + y

    status = problem.solve()

    print(f'Status: {LpStatus[status]}')
    for var in problem.variables():
        print(f'{var.name} = {var.value()}')
    print(f'objective = {problem.objective.value()}')


if __name__ == '__main__':
    main()
