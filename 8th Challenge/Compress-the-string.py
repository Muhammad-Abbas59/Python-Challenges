from itertools import groupby

def compress_string(s):
    compressed_string = ""
    for key, group in groupby(s):
        count = len(list(group))
        compressed_string += f"({count}, {key}) "

    return compressed_string.strip()

if __name__ == '__main__':
    s = input().strip()
    result = compress_string(s)
    print(result)
