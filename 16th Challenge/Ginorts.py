s = input()
def custom_sort(c):
    if c.islower():
        return (0, c)
    elif c.isupper():
        return (1, c)
    elif c.isdigit() and int(c) % 2 == 1:
        return (2, c)
    else:
        return (3, c)
result = ''.join(sorted(s, key=custom_sort))
print(result)