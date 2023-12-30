from itertools import product
def maximize_expression(n, m, lists):
    combinations = product(*lists)
    max_value = max(sum(x ** 2 for x in combination) % m for combination in combinations)
    return max_value
n, m = map(int, input().split())
lists = [list(map(int, input().split()[1:])) for _ in range(n)]
result = maximize_expression(n, m, lists)
print(result)