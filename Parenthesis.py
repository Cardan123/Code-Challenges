class Solution:
    def isValid(self, s: str) -> bool:
      stack = []

      for i in range(len(s)):
        
        c = s[i]
        
        if ( c == '(' or c == '{' or c == '[' ):
          stack.append(c)
          continue

        if(len(stack) == 0):
          return False

        top = stack.pop();

        

        if (c == ')' and (top == '{' or top == '[')):                     
          return False
        elif (c == '}' and (top == '(' or top == '[')): 
          return False
        elif (c == ']' and (top == '{' or top == '(')): 
          return False

      return len(stack) == 0



s = "(){}"

sol = Solution()

print(sol.isValid(s))