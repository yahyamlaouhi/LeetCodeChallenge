class Solution {
    public boolean isPalindrome(int x) {
        String string_number=String.valueOf(x);
        String[] list_number=string_number.split("");
   

        for(int i=0;i<list_number.length;i++){
            if  (!(list_number[i].equals(list_number[(list_number.length-1)-i]))){
                return false;
                
            }
        }
        return true;
        
        
        
        
        
    }
}