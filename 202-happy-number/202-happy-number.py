class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()
        while n not in visit:
           
            visit.add(n)
            
            n=self.sumOfSquares(n)
            if n==1:
                return 'true'
            
        return False

    def sumOfSquares(self,n:int)->int:
        s=0
        while n:
            num=n%10
            s=s+num**2
            n=n//10
        return s
        
            
        