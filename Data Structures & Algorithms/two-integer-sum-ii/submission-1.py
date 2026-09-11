class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # My Solution (Wrong)
        #index1 = 0;
        #index2 = 0;
        # Trying to make a hashmap/set of the numbers array first 
        #int sortednumbersarray = collections.defaultdict(numbers)
      
        #for index1 in range(len(sortednumbersarray)):
            #if ((sortednumbersarray[index1+1] != sortednumbersarray[index1]) 
            #and sortednumbersarray[index1+1] > sortednumbersarray[index]):
                #solution = []
                #solution.append(sortednumbersarray[index1], sortednumbersarray[index1+1])
                #print(solution)
                #return solution
                #return [sortednumbersarray[index1], sortednumbersarray[index1+1]]
        
        # Correct / Optimal solution using Two Pointer Algorithm
        left, right = 0, len(numbers) - 1

        while left < right:
            currentSum = numbers[left] + numbers[right] 
        
            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []