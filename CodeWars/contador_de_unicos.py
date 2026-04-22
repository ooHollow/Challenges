from collections import Counter
def find_unique(numbers: list):
    counts = Counter(numbers)
    for n in numbers:
        if counts[n] == 1:
            return n
    return None