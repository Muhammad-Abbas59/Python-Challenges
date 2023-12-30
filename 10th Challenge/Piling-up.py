def check_stack_possibility(n, blocks):
    left = 0
    right = n - 1
    top = float('inf')
    while left <= right:
        if blocks[left] >= blocks[right] and blocks[left] <= top:
            top = blocks[left]
            left += 1
        elif blocks[right] >= blocks[left] and blocks[right] <= top:
            top = blocks[right]
            right -= 1
        else:
            return "No"
    return "Yes"
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        blocks = list(map(int, input().split()))
        result = check_stack_possibility(n, blocks)
        print(result)