class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        def dfs(r, c):
            if image[r][c] == self.color:
                image[r][c] = newColor
                if r < self.row - 1:
                    dfs(r + 1, c)
                if c < self.column - 1:
                    dfs(r, c + 1)
                if r > 0:
                    dfs(r - 1, c)
                if c > 0:
                    dfs(r, c - 1)

        self.row = len(image)
        self.column = len(image[0])
        self.color = image[sr][sc]
        if self.color == newColor:
            return image
        dfs(sr, sc)
        return image


if __name__ == '__main__':
    s = Solution()
    print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
    print(s.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=1, sc=1, newColor=1))
    print(s.floodFill(image=[[0, 0, 0], [0, 1, 1]], sr=0, sc=0, newColor=1))
