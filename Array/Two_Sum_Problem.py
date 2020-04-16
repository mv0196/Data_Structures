#given a sorted array in accending order
#return 2 numbers that sum to a given number
#same element should not b used twice
import datetime
start = datetime.datetime.now()
# your code here
def two_sum(arr,n):
    if n>sum(arr[-2:]):
        return []
    elif n==sum(arr[-2:]):
        return [arr[-1],arr[-1]]
    i=0
    while i<len(arr) and n>(arr[i]+arr[i]):
        j=i+1
        while j<len(arr):
            if arr[i]+arr[j]==n:
                return [arr[i],arr[j]]
            j+=1
        i+=1
    return []

print(two_sum([-2,1,2,4,7,11],6))
print("Time taken:",datetime.datetime.now() - start)


"""
# YouTube Video: https://www.youtube.com/watch?v=gCin6Qz-eJQ
# Given an array of integers, return the two numbers such that they add up to
# a specific target. You may assume that each input would have exactly one
# solution, and you may not use the same element twice.

A = [-2, 1, 2, 4, 7, 11]
target = 13

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def two_sum_brute_force(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_hash_table(A, target):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


# Time Complexity: O(n)
# Space Complexity: O(1)
def two_sum(A, target):
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            print(A[i], A[j])
            return True
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return False


print(two_sum_brute_force(A, target))
print(two_sum_hash_table(A, target))
print(two_sum(A, target))
"""
