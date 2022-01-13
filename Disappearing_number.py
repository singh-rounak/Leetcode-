
 

class Solution(object):
	def findDisappearedNumbers(self, nums):
 		Out = []
 		N = set(nums)
 		n = len(nums)
 		for i in range(1, n+1):
 			if i not in N:
 				Out.append(i)
 		return Out

nums = [4,3,2,7,8,2,3,1]

Object  = Solution()
print(Object.findDisappearedNumbers(nums))

