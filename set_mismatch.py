# 645. Set Mismatch
# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
# You are given an integer array nums representing the data status of this set after the error.
# Find the number that occurs twice and the number that is missing and return them in the form of an array.

def findErrorNums(nums):
    n = len(nums)
    dup = None
    missing = None
    numsdict = Counter(nums)
            
    for i in range(1,n+1):
        if i in numsdict:
            if numsdict[i] > 1:
                dup = i
        else:
            missing = i
            
    return [dup, missing]

nums = [1,2,2,4]
print(findErrorNums(nums))

# Output: [2,3]

# Time Complexity: O(n)
# Space Complexity: O(n)