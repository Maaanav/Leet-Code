class Solution {
    public String orderlyQueue(String s, int k) {
        if(k==1){
            String smallest = s;
            for(int i =1; i<s.length(); i++){
                String rotation = s.substring(i) + s.substring(0, i);
                if (rotation.compareTo(smallest) < 0) {
                    smallest = rotation;
                }
            }
            return smallest;
            } else{
                char[] charArray = s.toCharArray();
            Arrays.sort(charArray);
            return new String(charArray);
            }
        }
}
