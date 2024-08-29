class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int i =0;
        while(i<nums.length){
            int correct = nums[i] - 1;
            if(nums[i] != nums[correct]){
                swap(nums, i, correct);
            } else{
                i++;
            }
        }
        ArrayList<Integer> res = new ArrayList<>();
        for(int in=0; in<nums.length; in++){
            if(nums[in] != in+1){
                res.add(in+1);
            }
        }

        return res;
    }

    private void swap(int[] nums, int first, int second){
        int temp = nums[first];
        nums[first] = nums[second];
        nums[second] = temp;
    }
}
