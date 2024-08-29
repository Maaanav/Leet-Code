class Solution {
    public int mySqrt(int x) {
        if(x == 0 || x == 1){
            return x;
        }

        int lf = 1, rg = x, ans =0;
        while(lf<=rg){
            int mid = lf + (rg-lf)/2;
            if(mid <= x/mid){
                ans = mid;
                lf = mid+1;
            }
            else{
                rg = mid-1;
            }
            
        }
        return ans;
    }
}
