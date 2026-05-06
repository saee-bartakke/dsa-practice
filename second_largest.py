#Problem : Second Largest
#Platform : GFG
#Link:https://www.geeksforgeeks.org/problems/second-largest3735/1
class Solution:
    def getSecondLargest(self, nums):
        # Code Here
        largest = float('-inf')
        
        #first traversal -> largest
        for num in nums:
            if num > largest:
                largest = num
                
        second_largest = float('-inf')
        
        
        for num in nums:
            if num != largest and num > second_largest:
                second_largest = num
                
        if second_largest == float('-inf'):
            return -1
        
                
        return second_largest
        