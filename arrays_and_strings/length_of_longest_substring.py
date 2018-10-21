"""
Prompt:

Given a string, find the length of the longest substring without repeating
characters.
"""
"""
start, end = 0, 0

[a, b, c, a, b, c, d]
          s
    e

[a b c b d]
     s
       e

[p, w, w, k, e, w]
       s
       e

o h v e h j d m l
    s

        e

"""


def length_of_longest_substring(s):
    cache = [0] * 256

    start = 0
    longest = 0
    for i in range(len(s) + 1):
        if i == len(s):
            longest = max(longest, i - start)
            break
        c_position = ord(s[i])
        if cache[c_position] == 0:
            cache[c_position] = 1
        else:
            longest = max(longest, i - start)
            while s[start] != s[i]:
                cache[ord(s[start])] = 0
                start += 1
            # if they are equal, dont want to advance start otherwise you do
            if start < i:
                start += 1
            else:
                start = i
                cache[c_position] = 1
    return longest


test_cases = [
    ("abcabcd", 4),
    ("au", 2),
    ("bbbbb", 1),
    (" ", 1),
    ("ohvhjdml", 6),
]

if __name__ == "__main__":
    for test_input, expected_output in test_cases:
        actual_output = length_of_longest_substring(test_input)
        if actual_output != expected_output:
            print("Didnt get right output: {} {}, got {}".format(
                test_input, expected_output, actual_output))
