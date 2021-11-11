class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j = len(s) - 1
        for i in range(0,len(s)//2):
            a = s[i]
            s[i] = s[j]
            s[j] = a
            j = j - 1
            