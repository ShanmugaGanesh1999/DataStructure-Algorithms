"""
#O(n^2)
def maxSubArraySum(a, s):
    if s > len(a):
        return None
    m = float("-inf")
    for i in range(len(a) - s + 1):
        k = 0
        for j in range(s):
            k += a[i + j]
        if m < k:
            m = k
    return m
"""


# O(n) - Sliding Window
def maxSubArraySum(a, s):
    if s > len(a):
        return None
    m = sum(a[:s])
    k = m
    for i in range(s, len(a)):
        k += a[i] - a[i - s]
        if m < k:
            m = k
    return m


a, s = [4, 2, 1, 6], 1  # 6
# a, s = [4, 2, 1, 6, 2], 4  # 13
# a, s = [], 4  # None
# a, s = [1, 2, 5, 2, 8, 1, 5], 2  # 10
# a, s = [1, 2, 5, 2, 8, 1, 5], 4  # 17
print(maxSubArraySum(a, s))


"""
#minSubArrayLen Solution
function minSubArrayLen(nums, sum) {
  let total = 0;
  let start = 0;
  let end = 0;
  let minLen = Infinity;

  while (start < nums.length) {
    // if current window doesn't add up to the given sum then 
		// move the window to right
    if(total < sum && end < nums.length){
      total += nums[end];
			end++;
    }
    // if current window adds up to at least the sum given then
		// we can shrink the window 
    else if(total >= sum){
      minLen = Math.min(minLen, end-start);
			total -= nums[start];
			start++;
    } 
    // current total less than required total but we reach the end, need this or else we'll be in an infinite loop 
    else {
      break;
    }
  }

  return minLen === Infinity ? 0 : minLen;
}

#findLongestSubstring Solution
function findLongestSubstring(str) {
  let longest = 0;
  let seen = {};
  let start = 0;

  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (seen[char]) {
      start = Math.max(start, seen[char]);
    }
    // index - beginning of substring + 1 (to include current in count)
    longest = Math.max(longest, i - start + 1);
    // store the index of the next char so as to not double count
    seen[char] = i + 1;
  }
  return longest;
}
"""
