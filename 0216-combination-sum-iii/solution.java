class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res, new ArrayList<>(), k, n, 1);
        return res; 
    }

    public void backtrack(List<List<Integer>> res,List<Integer> temp, int k, int rem, int start){
        if(temp.size() == k && rem == 0){
            res.add(new ArrayList<>(temp));
            return;
        }

        if(temp.size() > k || rem < 0){
            return;
        }

        for(int i =start; i<=9; i++){
            temp.add(i);
            backtrack(res, temp, k, rem-i, i+1);
            temp.remove(temp.size() - 1);
        }
    }
}
