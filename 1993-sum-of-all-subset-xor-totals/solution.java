class Solution {
    public int subsetXORSum(int[] nums) {
        return calXOR(nums,0,0);
    }

    private int calXOR(int[] nums, int index, int currXOR){
        if(index == nums.length){
            return currXOR;
        }

        int withelements = calXOR(nums, index+1, currXOR ^ nums[index]);
        int withoutelements = calXOR(nums, index+1, currXOR);

        return withelements + withoutelements; 
    }
}
