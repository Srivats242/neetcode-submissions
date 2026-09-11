class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # My Solution
        #sorted_nums_hashmap = collections.defaultdict(List[int])
        #return nums_hashmap
        #sorted_nums_hashmap = sorted(nums_hashmap)

        #result = []
        #sorted_nums = sorted(nums)
        #for i in range(len(sorted_nums)):
           #for j in range(len(sorted_nums)):
               #for k in range(len(sorted_nums)):
                #k = j + 1
                    #target = 0
                    #target = sorted_nums[j] + sorted_nums[k]

                    #j = 0
                    #k = len(sorted_nums) - 1
                    #target = -sorted_nums[i]
                    #target = sorted_nums[j] + sorted_nums[k]

                    #if (sorted_nums[j] + sorted_nums[k] < target):
                        #j = j + 1
                    #elif (sorted_nums[j] + sorted_nums[k] > target):
                        #k = k - 1
                    #elif (sorted_nums[j] + sorted_nums[k] == target):
                        #result.append(target)
                        #result.append(",".join(sorted_nums[j]))
                        #result.append(",".join(k))
                        #return [result]
                #if (sorted_sorted_nums_hashmap[i] + sorted_sorted_nums_hashmap[j] + sorted_sorted_nums_hashmap[k] == 0):
                    #return [[sorted_sorted_nums_hashmap[i], sorted_sorted_nums_hashmap[j], sorted_sorted_nums_hashmap[k]]]
                #else:
                    #return []
            
            # Hashmap
            #sorted_nums_hashmap = collections.defaultdict(sorted_nums)
            #target = -sorted_nums[i]

        #return 


        # Correct Solution

        result = []
        nums.sort()
        for index, value in enumerate(nums):

            if index > 0 and value == nums[index-1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                threeSum = value + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
        
     