class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lf = 0;
        int rig = numbers.length - 1;

        while(lf < rig){
            int ans = numbers[lf] + numbers[rig];
            if(ans == target){
                return new int[] {lf+1,rig+1};
            }else if(ans < target){
                lf++;
            }
            else{
                rig--;
            }

        }
        return new int[] {-1,-1};
        
    }
}
