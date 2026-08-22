class Solution {
    public boolean checkDivisibility(int n) {
        int su=0;
        int pr=1;
        int org=n;
        while (n>0){
            int digit=n%10;
            su+=digit;
            pr*=digit;
            n=n/10;
        }
        if (org % (su+pr)==0){
            return true;
        }
        return false;
    }
}