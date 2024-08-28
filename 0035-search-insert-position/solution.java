class Solution {
    public int searchInsert(int[] nums, int target) {

        int ans = BS(nums,target);
        return ans;
    }
    public int BS(int[] nums, int target){
        int start = 0;
        int end = nums.length-1;
        int ans = -1;
        while(start <= end)
        {
            int mid = start + (end-start)/2;

            if(nums[mid] > target){
                end = mid-1;
            } 
            else if(nums[mid] < target){
                ans = mid;
                start = mid+1;
            } else{
                return mid;
            }
        }
        
        return ans+1;
    }
}
