class Solution {
    public boolean predictTheWinner(int[] nums) {
        return help(nums,0,nums.length-1,1) >= 0;
    }

    public int help(int[] nums, int start, int end, int turn){
        if(start == end){
            return nums[start] * turn;
        }

        int st = nums[start] * turn + help(nums,start+1,end,-turn);
        int en = nums[end] * turn + help(nums,start,end-1,-turn);

        return Math.max(st*turn, en*turn) * turn;
    }
}
