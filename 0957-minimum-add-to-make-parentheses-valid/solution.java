class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> stack = new Stack<>();

        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c == ')' && !stack.isEmpty() && stack.peek() == '('){
                stack.pop();
            } else{
                stack.push(c);
            }
        }
        int res = 0;

        while(!stack.isEmpty()){
            stack.pop();
            res++;
        }

        return res;
    }
}
