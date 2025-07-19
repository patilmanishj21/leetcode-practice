# Merge Two Strings Alternately
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
 Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 
Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        res=[]
        while i< len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        # Append any remaining characters from either string
        res.append(word1[i:])
        res.append(word2[j:])
        return ''.join(res)

# s=Solution()
# print(s.mergeAlternately("abc", "pqr"))
# print(s.mergeAlternately("abcc", "pqr"))
# print(s.mergeAlternately("abcc", "pqrs"))



class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        c=''
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            c+= word1[i] + word2[i]
        c+=word1[min_len:] + word2[min_len:]
        return c

# s2=Solution2()
# print(s2.mergeAlternately("abclll", "pqrs"))




import time
word1 = "abc" * 1000000
word2 = "pqrs" * 1000000

s = Solution()
start = time.time()
s.mergeAlternately(word1, word2)
end = time.time()
print("Solution 1 time:", end - start)

s2 = Solution2()
start = time.time()
s2.mergeAlternately(word1, word2)
end = time.time()
print("Solution 2 time:", end - start)