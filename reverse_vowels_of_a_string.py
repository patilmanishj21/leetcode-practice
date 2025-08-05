'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"

Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

def reverseVowels(s):
            # Define vowels
            vowels = set("aeiouAEIOU")
            # Convert string to list for mutability
            s_list = list(s)
            # Two-pointer approach
            left, right = 0, len(s) - 1

            while left < right:
                # Move left pointer until a vowel is found
                while left < right and s_list[left] not in vowels:
                    left += 1
                # Move right pointer until a vowel is found
                while left < right and s_list[right] not in vowels:
                    right -= 1
                # Swap vowels
                if left < right:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    left += 1
                    right -= 1

            # Convert list back to string and return
            return ''.join(s_list)

s = "leetcode"

print(reverseVowels(s=s))


