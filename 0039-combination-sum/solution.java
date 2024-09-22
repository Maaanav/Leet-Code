class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();

        backtrack(candidates,target,0,curr,res);
        return res;
    }

    public void backtrack(int[] candidates, int target, int start, List<Integer> currentCombination, List<List<Integer>> result ){
        if(target == 0){
            result.add(new ArrayList<>(currentCombination));
            return;
        }

        if(target<0){
            return;
        }

        for(int i = start; i< candidates.length; i++){
            currentCombination.add(candidates[i]);
            backtrack(candidates, target-candidates[i], i, currentCombination, result);
            currentCombination.remove(currentCombination.size() - 1);
        }

    }
}
