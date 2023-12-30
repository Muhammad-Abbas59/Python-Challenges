if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # Sort the data based on the k-th attribute using lambda function
    sorted_arr = sorted(arr, key=lambda x: x[k])

    # Print the sorted data
    for row in sorted_arr:
        print(*row)
