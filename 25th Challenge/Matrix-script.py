import re
matrix = []
rows, columns = map(int, input().split())
for _ in range(rows):
    matrix.append(list(input()))
matrix = list(zip(*matrix))
decoded_script = ''
for subset in matrix:
    decoded_script += ''.join(subset)
result = re.sub(r'(?<=\w)([^\w\d]+)(?=\w)', ' ', decoded_script)
print(result)