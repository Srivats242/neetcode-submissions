class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      
      #numbers hashmap
      nums = {}
      nums[0] = 1
      nums[1] = 2
      nums[2] = 3
      
      #for i in range len(nums_hashmap_length):
      for key, value in nums.items():
        #if nums_hashmap[i] == nums_hashmap[i+1]:
            #return True
        print(f"Key {key}, Value {value}")
        print(f"Key {key + 1}, Value {value + 1}")
        print(f"Key {key + 2}, Value {value + 2}")
        print(f"Key {key + 3}, Value {value +2}")
        if (nums[key] == nums[key + 1]):
            return True
        else: 
            return False


      
