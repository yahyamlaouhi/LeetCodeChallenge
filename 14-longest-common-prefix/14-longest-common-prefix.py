class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=''
        for i in range(len(strs[0])):
            for j in strs:
                if len(j)==i or strs[0][i]!=j[i]  :
                   
                    return prefix
                
            prefix=prefix+strs[0][i]
        return prefix
                
                    
                    
        