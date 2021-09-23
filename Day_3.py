class Solution:
    def smallestpositive(self, array, n): 
        # Your code goes here
        array.sort()
        ans =1
        for i in range(n):
            if(array[i] <= ans):
                ans = array[i] + ans
        
        return ans
