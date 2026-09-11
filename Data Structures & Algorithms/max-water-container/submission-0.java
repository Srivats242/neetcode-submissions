class Solution {
    public int maxArea(int[] heights) {
        // My Solution
        //int total_output = 0;
        // Temporary output for debugging to see what happens when 2 elements are not equal

        //int most_area_output = 0;
        // Two pointer algorithm
        //for (int i = 0; i < heights.length; i++){
          //  for (int j = i + 1; j < heights.length; j++){
            //    if (heights[i] == heights[j])
               //     total_output = heights[i] * heights[j];
                //else
                  //  total_output = heights[i] + heights[j];
                
            //}
        //}
        //}
        //for(int j = heights.length - 1; j --){


        //}
        //return total_output;
        //int left = 0;
        //int right = heights.length - 1;

        //while left < right {
            //left++;
            //right--;
        //}


        // Correct Solution
        int l = 0;
        int r = heights.length - 1;
        int result = 0;

        while (l < r) {
            int area = (r-l) * Math.min(heights[l], heights[r]);
            result = Math.max(result, area);

            if (heights[l] <= heights[r]){
                l += 1;
            }
            else {
                r -= 1;
            }
        }
        return result;
    }
}   
