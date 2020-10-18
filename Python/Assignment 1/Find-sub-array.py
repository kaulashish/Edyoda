# Given an array arr[] of integers and an integer K, the task is to find the greatest contiguous sub-array of size K.
#
# Sub-array X is said to be greater than sub-array Y if the first non-matching element in both the sub-arrays has a greater value in X than in Y.
#
# For example :
# Input: arr[] = [1, 4, 3, 2, 5], K = 4
# Output: 4 3 2 5
# Two subarrays are [1, 4, 3, 2] and [4, 3, 2, 5]. First non-matching element from array1 and array 2 : 1 and 4 as 4 is greater
# Hence, the greater one is [4, 3, 2, 5]
#
# Input Format:
#
# First line will have space separated elements of list. Second line contains value.
#
# Output Format:
#
# print the required list

arr = [1, 4, 3, 2, 5]
k = 3
arr2 = []

for i in range(0, len(arr) - k + 1):
    arr2.append(arr[i:i+k])
print(max(arr2, key = lambda x: x[0]))
