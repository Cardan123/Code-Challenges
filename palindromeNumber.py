class Solution:
    def isPalindrome(self, x: int) -> bool:
        if((x%10 == 0 and x!=0) or (x < 0)):
          return False

        palindrome = 0

        while (x > palindrome):
          palindrome = (palindrome * 10) + (x%10)
          x = x // 10 

        return palindrome == x or (palindrome//10) == x


number = int(input())

obj = Solution()
ans = obj.isPalindrome(number)

print(ans)