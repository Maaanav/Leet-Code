class Solution {
    public boolean canJump(int[] nums) {
     int n = nums.length;
     int max_r = 0;

     for(int i=0;i <n; i++){
        
        if(i>max_r){
            return false;
        }

        max_r = Math.max(max_r, i + nums[i]);
        if(max_r >= n-1){
        return true;
        }
        
     }
     return true;   
    }
}
