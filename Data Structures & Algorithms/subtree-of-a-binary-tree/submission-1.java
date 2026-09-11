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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {

        /* My Solution
        // Time: O(m * n) 
        // Space: O(m + n) 
        // m and n - # of nodes in root and subRoot respectively

        // Root and Subroot have left and right nodes as well as values in each node

        // Loop through Root and subRoot to compare node values
        int val;
        TreeNode left;
        TreeNode right;
        // Left and Right node value comparison
        if (root.val == subRoot.val){
            return true;
        }
        if ((root.left == subRoot.left) && (root.right == subRoot.right)) {
            return true;
        }

    }
    return (root.val = subRoot.val ? true : false);
    */

    // Correct Solution

    if (subRoot == null){
        return true;
    }

    if (root == null) {
        return false;
    }

    if (sameTree(root, subRoot)) {
        return true;
    }

    return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    public boolean sameTree(TreeNode root, TreeNode subRoot) {
        if (root == null && subRoot == null) {
            return true;
        }

        if (root != null && subRoot != null && root.val == subRoot.val) {
            return sameTree(root.left, subRoot.left) && sameTree(root.right, subRoot.right);
        }
        return false;
    }


    
}
