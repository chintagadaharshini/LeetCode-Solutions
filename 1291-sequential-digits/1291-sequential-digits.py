class Solution(object):
    def sequentialDigits(self, low, high):
        answer=[]
        digits="123456789"
        low_length=len(str(low))
        high_length=len(str(high))
        for length in range(low_length,high_length+1):
            for start in range(10-length):
                number=int(digits[start:start+length])
                if low<=number<=high:
                    answer.append(number)
        return answer
    
        