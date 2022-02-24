class Solution:
    def climbStairs(self, n: int) -> int:
      if(n == 0):
        return 1
      elif (n < 0):
        return 0
      else:
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairsDP(self, n: int) -> int:
      dp = [0] * (n + 1)
      dp[0] = 1
      dp[1] = 1


      for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

      return dp[n]


n = int(input())

obj = Solution()
ans = obj.climbStairsDP(n)

print(ans)