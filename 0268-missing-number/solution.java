class Solution {
    public int missingNumber(int[] nums) {
        int i = 0;
        while(i<nums.length){
            int correct = nums[i];
            if(nums[i] < nums.length && nums[i] != nums[correct]){
                swap(nums, i,correct);
            } else {
                i++;
            }
        }
        for(int in = 0; in<nums.length; in++){
            if(nums[in] != in){
                return in;
            }
        }
        return nums.length;
    }

    private void swap(int[] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}
