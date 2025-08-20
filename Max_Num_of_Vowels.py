'''
Given a string s and an integer k, return the maximum number of 
vowel letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

def maxNumOfVowels(s,k):
    left=0
    right=k
    vowels=['a','e','i','o','u']
    max_count=0

    while left<len(s)-k+1:
        count=0
        for i in s[left:right]:
            if i in vowels:
                count+=1
        if max_count<count:
            max_count=count
            count=0

        left+=1
        right+=1

    return max_count
        
def sol2(s,k):
    vowels = {'a','e','i','o','u'}
    count = 0
    max_count = 0

    # count vowels in the first window of size k
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count

    # slide the window
    for i in range(k, len(s)):
        # remove the effect of the character going out
        if s[i-k] in vowels:
            count -= 1
        # add the effect of the new character coming in
        if s[i] in vowels:
            count += 1
        # update max
        max_count = max(max_count, count)

    return max_count


# s = "abciiidef"
# k = 3

# s = "leetcode"
# k = 3

s = "aeiou"
k = 2

print(maxNumOfVowels(s,k))
print(sol2(s,k))