class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Strategy:
        # 1. Loop though the nums array 
        # 2. Compare preceeding and succeeding elements
        # 3. If preceding element is not 1 less than succeeding element,
        # we start buildng the sequence
        # 4. Define a hashset with default dict to check if there are duplicates
        # 5. Capture length of the sequence after comparing previous and succeding elements across the array
        # 6. Return that length
        # 7. Convert the array to hash set using default dict and (set) with collections.defaultdict(set)
        # Best time complexity recommended solution: O(n) time complexity - Linear Search

        #sequence1 = []
        #i = 0
        #j = 0
        #for i in range (len(nums)):
            #if (nums[i] < nums[i + 1] & nums[i+1] == nums[i] + 1):
                #for j in range (i+1, len(nums)):

                    #if (nums[i] < nums[j] & nums[j] == nums[i] + 1):
                    # Sequence Array
                        #sequence1.append(nums[i])
                        # Nums Hashset
                        #numshashmap = collections.defaultdict(set)
                        #if(nums[i] in len(numshashmap)):
                            #seqence.pop(nums[i])
        #return len(sequence1)
                    
        numSet = set(nums)
        longest = 0

        for n in nums:
            if(n-1) not in numSet:
                length = 0
                while (n+length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
                 
                
                    
                

    
                





        