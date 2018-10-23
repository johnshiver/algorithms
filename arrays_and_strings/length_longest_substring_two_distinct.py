"""
Given a string s , find the length of the longest substring t  that contains at
most 2 distinct characters.
"""

def length_longest_substring_two_distinct(s):

    if len(s) < 2:
        return len(s)

    distinct_chars = set()
    longest = 0
    start = 0
    for i, char in enumerate(s):
        if len(distinct_chars) < 2:
            distinct_chars.add(char)
        elif char in distinct_chars:
            continue
        elif char not in distinct_chars and len(distinct_chars) == 2:
            longest = max(longest, i - start)
            distinct_chars = set()
            distinct_chars.add(char)
            # if curr character is new, last character was in last set
            # start should be first consecutive occurence of prev character
            prev_char = s[i - 1]
            distinct_chars.add(s[i - 1])
            start = i - 1
            while s[start] == prev_char:
                start -= 1
            start += 1
            if start < 0:
                start = 0

    return max(longest, (i - start) + 1)


test_cases = [
    ("eceba", 3),
    ("ccaabbb", 5),
]

if __name__ == "__main__":

    for test_input, expected_output in test_cases:
        actual_output = length_longest_substring_two_distinct(test_input)
        if actual_output != expected_output:
            print("Didnt get right output: {} {}, got {}".format(
                test_input, expected_output, actual_output))
