class Solution {
    public boolean isHappy(int n) {
        int slow = n;
        int fast = n;
        
        do{
            slow = findNext(slow);
            fast = findNext(findNext(fast));
               
        }while(slow != fast);
        
        return slow == 1;
    }
    
    private int findNext(int num){
        int nextNum = 0;
        while(num > 0){
            int lastDigit = num%10;
            num = num/10;
            nextNum += lastDigit * lastDigit;
        }
        return nextNum;
    }
}