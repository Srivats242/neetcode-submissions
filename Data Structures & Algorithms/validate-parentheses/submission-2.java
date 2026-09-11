class Solution {
    public boolean isValid(String s) {
        // 2 Pointer Algorithm Approach attempt (My Solution)
        //String array = new String(s);
        
        //Trying to convert String to an Array
        //String[] array = s.split(",");

        // Can use char[] instead and .toCharArray() to convert it to 
        // Example: s = "[]"
        // array of chars for example: ['[', ']']
        // s.split(",") converts it to just ["[]"] which is just one element

        //int i = 0;
        //int j = array.length() - 1;
        //int j = array.length - 1;
        //boolean result = true;
        //while (i < j) {
            
            
           // i++;
           // j--;
            //if (array[i] == array[j]){
                
                //result = true;
           // }
           // else {
            //    result = false;
            //}
        //}
        //return result;

        // Correct Solution (Stack Approach)
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        for (char c : s.toCharArray()) {
            if (closeToOpen.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == closeToOpen.get(c)){
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}
