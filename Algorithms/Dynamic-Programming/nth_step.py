#!/usr/bin/env python3


'''
A child is climbing up the stairs and they can take 1 or 2 or 3 steps at
a single moment, Implement a method to count how many possible ways
the child can run up the stairs
'''

# Runtime = O(1) + O(1) + T(n-1) + T(n-2) + T(n-3) == O(3^n)


def brute_force(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return brute_force(n - 1) + brute_force(n - 2) + brute_force(n - 3)


# Runtime = O(1) + O(1) + O(1) + O(n) + O(1) == O(n)
def bottom_up(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    prev = [1, 2, 4]
    curr = 3
    while curr < n:
        total = prev[0] + prev[1] + prev[2]
        prev[0] = prev[1]
        prev[1] = prev[2]
        prev[2] = total
        curr += 1
    return prev[2]


# Runtime = O(1) + O(1) + O(1) + O(n) + O(1) == O(n)
def memoized(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = memoized(n - 1, memo) + memoized(n - 2, memo) + memoized(n - 3, memo)
        return memo[n]


def memo_wrapper(n):
    memo = list()
    for i in range(n + 1):
        memo.append(-1)
    soln = memoized(n, memo)
    return soln


def main():
    brute_force = False
    n = int(input())
    if brute_force:
        brute_force(n)
    else:
        memo_wrapper(n)
    # you could use n = map(int, input()) for python 2.x


assert(brute_force(5)) == 13
assert(bottom_up(5)) == 13
assert(memo_wrapper(5)) == 13
assert(brute_force(10)) == 274
assert(bottom_up(10)) == 274
assert(memo_wrapper(10)) == 274
assert(brute_force(-1)) == 0
assert(bottom_up(-1)) == 0
assert(memo_wrapper(-1)) == 0


if __name__ == '__main__':
    main()
