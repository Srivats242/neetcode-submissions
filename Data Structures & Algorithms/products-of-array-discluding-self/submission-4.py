class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # My Solution
        #output = []
        #prefix = []
        #suffix = []
        #for i in range(len(nums)):
            # len(nums) = number of elements in the nums array e.g. 4 or 5
            #for j in range(i+1, len(nums)):
                #for k in range(len(output)):
                    #if (output[k] == nums[i]):
                        #for l in range(i+1, len(nums)):
                            #output[k] = nums[j] * nums[l]
                        #output.append(output[k])
            #for j in range(i+1, len(nums)):
                #nums[i] = nums[j] * nums[j]
            #for j in range(i+1, len(nums)):
                #for k in range(i+2, len(nums)):
                    #nums[i] = nums[j] * nums[k]'''
            #prefix.append(nums[i])
        #for j in range(len(nums), 0):
            #suffix.append(nums[j])
        
        
        #output.append(nums[i])
                #nums[i+1] * nums[i+2] *nums[i+3] * nums[i].length()

        #return output

        # CORRECT SOLUTION

        # O(n) time complexity and O(1) memory complexity
        # Result output array with only 1s placed in the initial array (just so array contents aren't empty)
        res = [1] * (len(nums))
    
        # Initialize Prefix value with 1
        prefix = 1
        # Loop through nums array from left to right
        for i in range(len(nums)):
            # Initally store prefix values of 1 in the result output array
            res[i] = prefix
            # Prefix is multiplied by whatever value is in the nums array and stored in the result output array
            prefix *= nums[i]
        # Initialize Postfix value with 1    
        postfix = 1
        # Loops through nums array from right to left
        for i in range(len(nums) - 1 , -1 , -1):
            # Multiply the postfix value with the prefix values already stored in the result output array
            res[i] *= postfix
            # Multiply the nums array input values with postfix value which then multiplies the prefix values in the output array that were placed in it before (previous loop)
            postfix *= nums[i]
        # Return the final resulting output array that is created by both prefix and postfix values being multiplied by the input values in the nums array
        return res