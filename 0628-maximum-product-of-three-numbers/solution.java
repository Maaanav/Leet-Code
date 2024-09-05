class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length-1;
        int res1 = nums[0]*nums[1]*nums[n];
        int res2 = nums[n]*nums[n-1]*nums[n-2];

        int res = Math.max(res1,res2);
    
        return res;
    }
}
