'''
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets 
is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain
 any digits and that digits are only for those repeat numbers, 
 k. For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.
Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
'''


def DecodeString(s):
    stack=[]
    curr_str=''
    curr_num=0

    for char in s:
        if char.isdigit():
            curr_num=curr_num*10+ int(char)
        elif char =='[':
            stack.append((curr_str,curr_num))
            curr_str=''
            curr_num=0
        elif char ==']':
            prev_string,repeted_cnt=stack.pop()
            curr_str=prev_string+curr_str*repeted_cnt
        else:  
            curr_str += char
    return  curr_str

        
            
            

#s = "3[a]"
s = "3[a2[b]]"
#s = "2[abc]3[cd]ef"
print(DecodeString(s))