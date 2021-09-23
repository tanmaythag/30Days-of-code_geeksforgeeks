class Solution:
    def findNth(self,N):
        #code here
        s = ""
        while(N):
            s = str(N % 9) + s
            N = N // 9
        
        return int(s)
