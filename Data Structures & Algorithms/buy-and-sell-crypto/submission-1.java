class Solution {
    public int maxProfit(int[] prices) {

        // My Solution Strategy (Two Pointer Approach)
        /*int i = 0;
        int j = prices.length - 1;
        int profit = 0;


        while (i <= j){
         
            //int profit = prices[j] - prices[i];
            if (prices[i] < prices[j]){
                profit = prices[j] - prices[i];
                return profit;
            } else if (prices[i] == prices[j]){
                profit = prices[j] - prices[i];
                return profit;
                
            } else {
                profit = 0;
                return 0;
            }
        }
        return profit;*/

        // Correct Solution
        int left = 0;
        int right = 1;
        int maxProfit = 0;
        while (right < prices.length) {
            // Check if it is a profitable price or not
            if (prices[left] < prices[right]){
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            } else {
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}
