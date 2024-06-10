# O(n)
def isPalindrome(a):
    l, r = 0, len(a) - 1
    if r < 2:
        return True
    elif a[l] == a[r]:
        return isPalindrome(a[1:-1])
    else:
        return False


# a = "madam"
# a = "civic"
a = "newn"
print(isPalindrome(a))
