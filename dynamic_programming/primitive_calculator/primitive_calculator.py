# Uses python3
import sys


def dp_optimal_sequence(x):
    hop_count = [0] * (x + 1)
    hop_count[1] = 0
    for i in range(2, x+1):
        min_def = hop_count[i-1] + 1
        min_2, min_3 = sys.maxsize, sys.maxsize
        if i % 2 == 0:
            min_2 = hop_count[i//2] + 1
        if i % 3 == 0:
            min_3 = hop_count[i//3] + 1
        hop_count[i] = min(min_def, min_2, min_3)

    final_sequence = []
    final_sequence.append(x)
    min_2, min_3 = sys.maxsize, sys.maxsize
    while x >= 1:
        if x % 2 == 0:
            min_2 = hop_count[x//2]
        if x % 3 == 0:
            min_3 = hop_count[x//3]
        min_def = hop_count[x-1]

        smallest = min(min_def, min_2, min_3)
        if smallest == min_3:
            x = x // 3
            final_sequence.append(x)
        elif smallest == min_2:
            x = x // 2
            final_sequence.append(x)
        else:
            x -= 1
            final_sequence.append(x)
    final_sequence.pop()
    return reversed(final_sequence)


#input = sys.stdin.read()
n = int(input())
sequence = list(dp_optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
