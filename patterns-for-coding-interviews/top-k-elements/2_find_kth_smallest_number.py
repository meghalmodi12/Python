from heapq import *

def findKthSmallestNumber(nums, k):
    result = []

    for num in nums:
        heappush(result, num)

    while k - 1 > 0:
        heappop(result)
        k -= 1

    return heappop(result)