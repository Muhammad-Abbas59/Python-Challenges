from collections import Counter

def find_top_characters(s):
    # Count occurrences of each character
    char_count = Counter(s)

    # Sort by occurrence count (descending) and then alphabetically
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    # Print the top three characters and their counts
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")

if __name__ == '__main__':
    s = input()
    find_top_characters(s)
