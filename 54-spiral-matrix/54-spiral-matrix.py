class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralList=[]
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        while left<right and top <bottom:
            for i in range(left,right):
                spiralList.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                spiralList.append(matrix[i][right-1])
            right-=1
            if not(left<right and top <bottom):
                break
            
            for i in reversed(range(left,right)):
                spiralList.append(matrix[bottom-1][i])
            bottom-=1 
            for i in reversed (range(top,bottom)):
                spiralList.append(matrix[i][left])
            left+=1
            
            
        return spiralList
            