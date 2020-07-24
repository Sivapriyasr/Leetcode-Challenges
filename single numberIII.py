'''Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
'''

from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        return([i for i in count if count[i]==1])
        
