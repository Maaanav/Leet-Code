class Solution {
    public void sortColors(int[] nums) {
        int zero=0;
        int one=0;
        int two=0;
        for(int i=0; i<nums.length; i++){
            if(nums[i] == 0){
                zero++;
            } else if(nums[i] == 1){
                    one++;
                } else{
                    two++;
                }
            }

        for(int a = 0; a<zero; a++){
            nums[a] = 0;
        }
        for(int b = zero; b<one+zero; b++){
            nums[b] = 1;
        }
        for(int c = one+zero; c<nums.length; c++){
            nums[c] = 2;
        }
        }
}
