'''Given a set, find all of its subsets'''


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    print(tuple(pool[i] for i in indices))
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        print(tuple(pool[i] for i in indices))


def main():
    x = input().strip(' ')
    s = list()
    for i in range(1, len(x) + 1):
        s.append(combinations(x, i))
    print(s)


if __name__ == '__main__':
    main()
