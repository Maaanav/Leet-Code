class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if(image[sr][sc] == color){
            return image;
        }

        int og = image[sr][sc];
        dfs(image,sr,sc,og,color);
        return image;
    }

    public void dfs(int[][] image, int i, int j, int og, int newColor){

        if(i < 0 || i >= image.length || j < 0 || j >= image[i].length || image[i][j] != og){
            return;
        }

        image[i][j] = newColor;
        dfs(image, i+1, j, og, newColor);
        dfs(image, i, j+1, og, newColor);
        dfs(image, i-1, j, og, newColor);
        dfs(image, i, j-1, og, newColor);
    }
}
