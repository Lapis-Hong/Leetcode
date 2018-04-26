"""Prob 15. 3Sum

Description:
    Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
 [-1, 0, 1],
 [-1, -1, 2]
]
"""


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret =[]
    nums.sort()
    for i in range(len(nums)-2):
        n1 = nums[i]
        if n1 > 0:
            break
        for j in range(i+1, len(nums)-1):
            n2 = nums[j]
            if n1 + n2 > 0:
                break
            for k in range(j+1, len(nums)):
                n3 = nums[k]
                if n3 < 0 or n1 + n2 + n3 > 0:
                    break
                elif n1 + n2 + n3 == 0:
                    triplet = [n1, n2, n3]
                    if triplet not in ret:                      
                        ret.append(triplet)
    return ret

def threeSum2(nums):
    res = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

if __name__ == "__main__":
    print(threeSum([-1, 0, 1, 2, -1, -4]))
    print(threeSum2([-1, 0, 1, 2, -1, -4]))
