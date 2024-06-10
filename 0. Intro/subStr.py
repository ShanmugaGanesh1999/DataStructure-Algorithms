# O(n)
def isSubStr(a, b):
    if len(a) == 0:
        return True
    if len(b) == 0:
        return False
    i, j = 0, 0
    while j < len(b):
        if a[i] == b[j]:
            i += 1
        if i == len(a):
            return True
        j += 1
    return False


"""
function isSubsequence(str1, str2) {
  if(str1.length === 0) return true
  if(str2.length === 0) return false
  if(str2[0] === str1[0]) return isSubsequence(str1.slice(1), str2.slice(1))  
  return isSubsequence(str1, str2.slice(1))
}
"""

a, b = "234", "12345"  # true
print(isSubStr(a, b))
