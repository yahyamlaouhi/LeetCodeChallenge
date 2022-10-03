class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        # 1
        answer = [None] * len(grid[0])
        
        #2
        deadends = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])-1):
                if grid[row][col] == 1 and grid[row][col+1] == -1:
                    deadends.add((row, col))
                    deadends.add((row, col+1))
        
        #3
        for col in range(len(grid[0])):
            balls = col
            for row in range(len(grid)):
                #4
                if (row, col) in deadends:
                    answer[balls] = -1
                    break
                #5
                if not 0<=col<len(grid[0]):
                    answer[balls] = -1
                    break

                col = col+grid[row][col]
            
            #6
            if answer[balls] is None:
                if not 0<=col<len(grid[0]):
                    answer[balls] = -1
                else:
                    answer[balls] = col
        
        #7
        return answer
