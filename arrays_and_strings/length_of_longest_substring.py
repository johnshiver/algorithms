"""
Prompt:

Given a string, find the length of the longest substring without repeating
characters.
"""


def length_of_longest_substring(s):

	if len(s) < 2:
		return len(s)

	last_seen_cache = [-1]*256
	start = longest = 0
	for i, char in enumerate(s):
		pos = ord(char)
		last_seen = last_seen_cache[pos]
		if last_seen >= start:
			longest = max(longest, i-start)
			start = last_seen + 1
		last_seen_cache[pos] = i

	return max(longest, (i-start)+1)


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
