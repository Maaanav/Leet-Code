class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1;
        int high = Arrays.stream(piles).max().getAsInt();

        while(low<=high){
            int mid = low + (high - low)/2;
            if(koko(piles,h,mid)){
                high = mid-1;
            } else{
                low = mid+1;
            }
        }

        return low;
        
    }

    private boolean koko(int[] piles, int h, int k){
        int hour = 0;
        for(int pile : piles){
            hour += (pile + k -1)/k;
            if(hour > h){
                return false;
            }
        }
        return hour <= h;
    }
}
