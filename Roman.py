def romanToInteger(number = ""):
  m = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
  
  result = 0

  size = len(number) - 1


  for i in range(size):
    
    if (m[number[i]] < m[number[i+1]]):
      result += m[number[i+1]] - m[number[i]]
      i += 1
      continue

    result += m[number[i]]

  if(i != size):
    result += m[number[i]]

  return result 



inputNumber = (input())

print(romanToInteger(inputNumber.upper()))
