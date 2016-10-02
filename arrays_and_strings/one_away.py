"""
Problem taken from 6th edition of cracking the coding interview
"""


def one_away(s, t):
    """
    Given two strings, checks whether they are one edit (or zero edits)
    away from equality.

    Example:
      pale, ple     -> true
      pales, pale   -> true
      pale, bale    -> true
      pale, bake    -> false
    """

    ln_s = len(s)
    ln_t = len(t)

    if abs(ln_s - ln_t) > 1:
        return False
    if max(ln_t, ln_s) == 1 and ln_t != ln_s:
        return True

    i = j = error = 0
    while i < ln_s and j < ln_t:
        if s[i] != t[j]:
            error += 1
            if ln_s > ln_t:
                i += 1
            elif ln_s < ln_t:
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return error == 1 or (error == 0 and abs(ln_s - ln_t) == 1)


if __name__ == '__main__':
    s1 = 'bake'
    s2 = 'pale'
    print(s1, s2)
    print(one_away(s1, s2))

    s1 = 'pale'
    s2 = 'ple'
    print(s1, s2)
    print(one_away(s1, s2))

    s1 = 'pales'
    s2 = 'pale'
    print(s1, s2)
    print(one_away(s1, s2))

    s1 = 'a'
    s2 = 'ba'
    print(s1, s2)
    print(one_away(s1, s2))

