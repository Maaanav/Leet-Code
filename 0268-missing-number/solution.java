class Solution {
    public int missingNumber(int[] nums) {
        int size = nums.length;
        int temp = 0;
        Arrays.sort(nums);
        for(int i=0; i<size; i++){
            if(nums[i] != temp)
            return temp;
            temp++;
        }
        return temp;
    }
}
