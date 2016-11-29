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


def get_subsets(iterable):
    if iterable is None:
        return None
    subsets = [[]]
    new_set = []
    for n in iterable:
        for s in subsets:
            new_set.append(s + [n])
        subsets += new_set
        new_set = []
    print(subsets)


def main():
    x = list(map(int, input().split(' ')))
    get_subsets(x)


if __name__ == '__main__':
    main()
