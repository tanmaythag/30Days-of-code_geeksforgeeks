class Solution:
    def prank(self, a, n): 
        #code here
        for i in range(n):
            a[i] = a[i] + (a[a[i]]%n) * n
        
        for i in range(n):
            a[i] = a[i] // n
