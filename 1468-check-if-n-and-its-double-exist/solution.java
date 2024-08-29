class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> hs = new HashSet<>();

        for(int num : arr){
            if(hs.contains(2*num) || (num % 2 == 0 && hs.contains(num/2))){
                return true;
            } else{
                hs.add(num);
            }
        }
        return false;
    }
}
