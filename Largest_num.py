'''
QUESTION: Given a number of integers, combine them so it would create the largest number.
'''


def largestNum(nums):
   
    if nums == [0]*len(nums):
        return "0"
    
    #inplace swapping from highest to lowest 2 digit numbers
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            num1 = int(str(nums[i]) + str(nums[j]))
            num2 = int(str(nums[j]) + str(nums[i]))
            
            if num2 > num1:
                swap(nums,i,j)
    
	ans = ""
    for i in nums:
        ans += str(i)    
    return ans
    
	
def swap(arr,i,j):
	arr[i], arr[j] = arr[j],arr[i]


 
#print(largest([54, 546, 548, 60]))
"""
Time : O(N^2)
Space : O(1)
"""

print largestNum([17, 7, 2, 45, 72])

"""
from itertools import permutations
def largestNum(l):
    lst = []
    for i in permutations(l, len(l)):
        # provides all permutations of the list values,
        # store them in list to find max
        lst.append("".join(map(str,i)))

    return max(lst)

# 77245217
Time : O(NlogN)
Space : O(1)
"""