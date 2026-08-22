class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        def dfs(image: List[list[int]], r: int, c: int, newcolor: int, oldcolor: int):
            if r < 0 or c < 0 or r >= m or c >= n or image[r][c] == newcolor or image[r][c] != oldcolor:
                return
            image[r][c] = newcolor

            dfs(image,r+1,c,newcolor,oldcolor)
            dfs(image,r,c+1,newcolor,oldcolor)
            dfs(image,r-1,c,newcolor,oldcolor)
            dfs(image,r,c-1,newcolor,oldcolor)
        
        dfs(image,sr,sc,color,image[sr][sc])
        return image
