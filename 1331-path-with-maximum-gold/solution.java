class Solution {
    public int getMaximumGold(int[][] grid) {
        int max = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] > 0){
                    max = Math.max(max, collGold(grid,i,j));
                }
            }
        }

        return max;
         
    }

    private int collGold(int[][] grid, int i, int j){
        if(i<0 || i >= grid.length || j<0 || j >= grid[0].length || grid[i][j] == 0){
            return 0;
        }

        int currGold = grid[i][j];
        grid[i][j] = 0;

        int up = collGold(grid, i-1,j);
        int down = collGold(grid, i+1, j);
        int right = collGold(grid, i, j+1);
        int left = collGold(grid, i, j-1);

        grid[i][j] = currGold;

        return currGold + Math.max(Math.max(up,down),Math.max(right,left));
    }


}
