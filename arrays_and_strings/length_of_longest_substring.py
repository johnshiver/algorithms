

def length_of_longest_substring(s):
    """Finds length of longest substring without repeating characters.

    :param s:
    :return:
    """
    i = j = 0
    chars = set()
    longest = 0
    while j < len(s):
        if s[j] not in chars:
            chars.add(s[j])
            j += 1
        else:
            longest = max(longest, len(chars))
            # get rid of current char because it's a dupe
            # re-added on next loop
            chars.remove(s[j])
            # move first pointer to dupe char
            # and pop chars off set
            while s[i] != s[j]:
                chars.remove(s[i])
                i += 1
            i += 1
    return max(longest, len(chars))

if __name__ == "__main__":
    print length_of_longest_substring("advd")
