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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        //TreeNode w = new TreeNode(0);
        //TreeNode curr = p(0);
        // My Solution (Wrong)
        /*for (int i = 0; i < p.length(); i++){
            for (int j = 0; j < q.length(); j++){
                if (p.length() != q.length()){
                    return false;
                }
                else {
                    return true;
                }
                
            }
        }*/
        if (p == null && q == null){
            return true;
        }
        if (p != null && q != null && p.val == q.val){
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        } else {
            return false;
        }
    }
}
