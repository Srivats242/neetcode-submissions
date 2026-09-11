/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isBalanced(TreeNode root) {

        // My Solution (Wrong)
        // Left subtree: root.left
        // Right subtree: root.right
        
        // Base case: If root is empty or null, return true
        /*if (root == null) {
            return true;
        }

        /*if (root.length == 0){
            return true;
        }*/
        /*if (root != null && root.left != null && root.right != null){
            return isBalanced(root.left) && isBalanced(root.right);
        } else if (root != null && root.left == null || root.right == null) {
            return false;
        }
        else {
            return true;
        }*/

        // Correct Solution
        return dfs(root)[0] == 1;
        }
        private int[] dfs(TreeNode root){
            if (root == null){
                return new int[]{1, 0};
            }

            int[] left = dfs(root.left);
            int[] right = dfs(root.right);

            boolean balanced = (left[0] == 1 && right[0] == 1) && (Math.abs(left[1] - right[1]) <= 1);
            int height = 1 + Math.max(left[1], right[1]);

            return new int[]{balanced ? 1: 0, height};
        }

    
}
