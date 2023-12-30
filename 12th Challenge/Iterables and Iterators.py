from itertools import combinations

def probability_of_letter_a(length, letters, num_indices):
    indices = list(range(1, length + 1))
    indices_combinations = list(combinations(indices, num_indices))

    count_a_not_present = 0

    for combination in indices_combinations:
        if 'a' not in [letters[i - 1] for i in combination]:
            count_a_not_present += 1

    probability = count_a_not_present / len(indices_combinations)
    return round(1 - probability, 4)

# Input reading
length = int(input())
letters = input().split()
num_indices = int(input())

# Calculate and print the probability
result = probability_of_letter_a(length, letters, num_indices)
print(result)