
def permute(word):
    if len(word) == 1:
        return [word]

    result = []
    for i, v in enumerate(word):
        result += [v+p for p in permute(word[:i] + word[i+1:])]
    return result

if __name__ == '__main__':
    print(permute('abc'))
