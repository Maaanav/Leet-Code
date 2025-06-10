class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder sb = new StringBuilder();

        for(char c: s.toCharArray()){
            if(Character.isLetterOrDigit(c)){
                sb.append(Character.toLowerCase(c));
            }
        }
        String p = sb.toString();
        int left =0;
        int right = p.length()-1;

        while(left<right){
            if(p.charAt(left) != p.charAt(right)){
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
