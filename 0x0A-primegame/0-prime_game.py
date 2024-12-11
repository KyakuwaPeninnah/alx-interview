#!/usr/bin/python3
"""task1"""


def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    fltr = [True for _ in range(max(n + 1, 2))]
    for k in range(2, int(pow(n, 0.5)) + 1):
        if not fltr[k]:
            continue
        for j in range(k * k, n + 1, k):
            fltr[j] = False
    fltr[0] = fltr[1] = False
    c = 0
    for k in range(len(fltr)):
        if fltr[k]:
            c += 1
        fltr[k] = c
    plyr1 = 0
    for n in nums:
        plyr1 += fltr[n] % 2 == 1
    if plyr1 * 2 == len(nums):
        return None
    if plyr1 * 2 > len(nums):
        return "Maria"
    return "Ben"
