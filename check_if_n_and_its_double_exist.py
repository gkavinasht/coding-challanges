# 1346. Check If N and Its Double Exist
# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

def checkIfExist(arr):
    arrDict = {}
    for i in range(len(arr)):
        if 2 * arr[i] in arrDict:
            return True
        elif arr[i] % 2 == 0:
            if arr[i] / 2 in arrDict:
                return True
        arrDict[arr[i]] = 1
        
    return False

arr = [10,2,5,3]
print(checkIfExist(arr))

# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Time Complexity : O(n)
# Space Complexity: O(n)
