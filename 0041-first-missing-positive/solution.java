class Solution {
    public int firstMissingPositive(int[] nums) {
        int i=0;
        while(i<nums.length){
            int correct = nums[i] - 1;
            if(nums[i] > 0 && nums[i] <= nums.length && nums[i] != nums[correct]){
                swap(nums,i, correct);
            }else{
                i++;
            }
        }

        for(int in=0;in<nums.length; in++){
            if(nums[in] != in+1){
                return in+1;
            }
        }
        return nums.length+1;
    }

    private void swap(int[] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
     }
}
