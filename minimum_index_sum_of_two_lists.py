# 599. Minimum Index Sum of Two Lists
# Given two arrays of strings list1 and list2, find the common strings with the least index sum.
# A common string is a string that appeared in both list1 and list2.
# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
# Return all the common strings with the least index sum. Return the answer in any order.

def findRestaurant(list1, list2):
    res = []
    min_index = float(inf)
    map2 = {}

    for i in range(len(list2)):
        map2[list2[i]] = i

    for i in range(len(list1)):
        if list1[i] in list2:
            sum_of_indexes = i + map2[list1[i]]
            if min_index > sum_of_indexes:
                min_index = sum_of_indexes
                res = [list1[i]]
            elif min_index == sum_of_indexes:
                min_index = sum_of_indexes
                res.append(list1[i])

    return res

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

print(findRestaurant(list1, list2))

# Time Complexity: O(m+n)
# Space Complexity: O(n)

# Output: ["Shogun"]
# Explanation: The only common string is "Shogun".