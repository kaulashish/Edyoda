# Given a list of N integers. The task is to eliminate the minimum number of elements such that in the resulting list the sum of any two adjacent values is even.
#
# Numbers = [1, 3, 5, 4, 2]
# Output = [1, 3, 5]
# Total elements removed 2
# Elements to be removed [4,2]
#
# Input Format:
#
# One line containe space separated list elements
#
# Output Format:
#
# print the result list
#
# Sample Input 0:
# 1 3 5 4 2
#
# Sample Output 0:
# [1, 3, 5]

import copy
arr = [1,2,2,4,3]
nested_array = []

for i in range(0, len(arr)-1):
    z = copy.deepcopy(i)
    arr2 = []
    for j in range(z + 1, len(arr)):
        if (arr[z] + arr[j]) % 2 == 0:
            if arr[z] not in arr2:
                arr2.append(arr[z])
            arr2.append(arr[j])
            z = j
    nested_array.append(arr2)

print(max(nested_array, key = len))
