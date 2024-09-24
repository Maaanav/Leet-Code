class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();

        helpfunc(res, new ArrayList<>(),candidates,target,0);

        return res;
    }

    private void helpfunc(List<List<Integer>> res, List<Integer> templist, int[] candidates, int rem, int start){

        if(rem == 0){
            res.add(new ArrayList<>(templist));
            return;
        }

        for(int i=start; i<candidates.length; i++){
            if(i > start && candidates[i] == candidates[i-1]) continue;
            if(candidates[i] > rem) break;

            templist.add(candidates[i]);
            helpfunc(res, templist, candidates, rem - candidates[i], i+1);
            templist.remove(templist.size() - 1);
        }

    }
}
