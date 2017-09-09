

def isPalindrome(str):
  for i in range(int(len(str)/2)):
    if str[i]!= str[len(str)-1-i]:
      return False
  return True
  
def longestPalindrome(str):
  for i in range(len(str),-1,-1):
    for j in range(len(str)-i):
      if isPalindrome(str[j:j+i]):
        return str[j:j+i]

print(longestPalindrome('dwwgwdt'))