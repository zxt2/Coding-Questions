'''
## Pattern: Sliding Window
'''

'''
1. Maximum Sum Subarray of Size K

Problem Statement #  
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.  

Example 1:  
Input: [2, 1, 5, 1, 3, 2], k=3   
Output: 9  
Explanation: Subarray with maximum sum is [5, 1, 3].  

Example 2:  
Input: [2, 3, 4, 1, 5], k=2   
Output: 7  
Explanation: Subarray with maximum sum is [3, 4].
'''

def max_sub_array_of_size_k(nums, k):
    windowsum = sum(nums[:k])
    maxsum = windowsum
    for i in range(len(nums)-k):
        windowsum = windowsum-nums[i]+nums[i+k]
        maxsum = max(maxsum,windowsum)
    return maxsum


'''
2. Smallest Subarray with a given sum

Problem Statement #  
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.  

Example 1:  
Input: [2, 1, 5, 2, 3, 2], S=7   
Output: 2  
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].  

Example 2:  
Input: [2, 1, 5, 2, 8], S=7   
Output: 1  
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].  

Example 3:  
Input: [3, 4, 1, 1, 6], S=8   
Output: 3  
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].  
'''

def smallest_subarray_with_given_sum(nums,S):
    if sum(nums) < S:
        return 0
    l = 0
    windowsum = 0
    minlen = len(nums)
    for r in range(len(nums)):
        windowsum += nums[r]
        while windowsum-nums[l]>=S:
            windowsum -= nums[l]
            l += 1
        if windowsum >= S:
            minlen = min(minlen, r-l+1)
    return minlen

'''
3. Longest Substring with K Distinct Characters  

Problem Statement #  
Given a string, find the length of the longest substring in it with no more than K distinct characters.  

Example 1:  
Input: String="araaci", K=2  
Output: 4    
Explanation: The longest substring with no more than '2' distinct characters is "araa".  

Example 2:  
Input: String="araaci", K=1  
Output: 2  
Explanation: The longest substring with no more than '1' distinct characters is "aa".  

Example 3:  
Input: String="cbbebi", K=3  
Output: 5  
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".  
'''

def longest_substring_with_k_distinct(s, k):
    l = 0
    dic = {}
    maxlen = 0
    for r in range(len(s)):
        if s[r] not in dic:
            dic[s[r]] = 1
        else:
            dic[s[r]] += 1
        while len(dic) > k:
            dic[s[l]] -= 1
            if dic[s[l]] == 0:
                del dic[s[l]]
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen

'''
4. Fruits into Baskets  

Problem Statement #  
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.  
You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.  
Write a function to return the maximum number of fruits in both the baskets.  

Example 1:  
Input: Fruit=['A', 'B', 'C', 'A', 'C']  
Output: 3  
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']  

Example 2:  
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']  
Output: 5  
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.   
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']  
'''
def fruits_into_baskets(Fruit):
    l = 0
    dic = {}
    maxfruit = 0
    for r in range(len(Fruit)):
        if Fruit[r] not in dic:
            dic[Fruit[r]] = 1
        else:
            dic[Fruit[r]] += 1
        if len(dic)>2:
            dic[Fruit[l]] -= 1
            if dic[Fruit[l]] == 0:
                del dic[Fruit[l]]
            l += 1
        maxfruit = max(maxfruit, sum(dic.values()))
    return maxfruit


'''
5. No-repeat Substring  

Problem Statement #  
Given a string, find the length of the longest substring which has no repeating characters.  

Example 1:  
Input: String="aabccbb"  
Output: 3  
Explanation: The longest substring without any repeating characters is "abc".  

Example 2:  
Input: String="abbbb"  
Output: 2  
Explanation: The longest substring without any repeating characters is "ab".  

Example 3:  
Input: String="abccde"  
Output: 3  
Explanation: Longest substrings without any repeating characters are "abc" & "cde". 
'''
def non_repeat_substring(s):
    l = 0
    dic = {}
    maxlen = 0
    for r in range(len(s)):
        if s[r] not in dic:
            dic[s[r]] = 1
        else:
            dic[s[r]] += 1
        while dic[s[r]] > 1:
            dic[s[l]] -= 1
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen

# answer
def non_repeat_substring2(s):
    l = 0
    maxlen = 0
    dic = {}   # dict records the last index of ‘key’
    for r in range(len(s)):
        if s[r] in dic:
            l = max(l, dic[s[r]]+1)
        dic[s[r]] = r
        maxlen = max(maxlen, r-l+1)
    return maxlen

'''
6. Longest Substring with Same Letters after Replacement

Problem Statement #  
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.  

Example 1:  
Input: String="aabccbb", k=2  
Output: 5  
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".  

Example 2:  
Input: String="abbcb", k=1  
Output: 4  
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".  

Example 3:  
Input: String="abccde", k=1  
Output: 3  
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".  
'''

def length_of_longest_substring(s, k):
    l = 0
    dic = {}
    maxlen = 0
    for r in range(len(s)):
        if s[r] not in dic:
            dic[s[r]] = 1
        else:
            dic[s[r]] += 1
        while r-l+1-max(dic.values()) > k:
            dic[s[l]] -= 1
            if dic[s[l]] == 0:
                del dic[s[l]]
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen

'''
7. Longest Subarray with Ones after Replacement 

Problem Statement #  
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.  

Example 1:  
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2  
Output: 6  
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.  

Example 2:   
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3  
Output: 9  
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.  
'''

def length_of_longest_substring(nums, k):
    l = 0
    maxlen = 0
    numberone = 0
    for r in range(len(nums)):
        if nums[r] == 1:
            numberone += 1
        while r-l+1-numberone > k:
            if nums[l] == 1:
                numberone -= 1
            l += 1
        maxlen = max(maxlen,r-l+1)
    return maxlen

'''
8. Problem Challenge 1 *Permutation in a String

Problem Challenge 1 #  
Permutation in a String (hard)   
Given a string and a pattern, find out if the string contains any permutation of the pattern.  
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:  
abc, acb, bac, bca, cab, cba  
If a string has ‘n’ distinct characters it will have n!n! permutations.  

Example 1:  
Input: String="oidbcaf", Pattern="abc"  
Output: true  
Explanation: The string contains "bca" which is a permutation of the given pattern.  

Example 2:  
Input: String="odicf", Pattern="dc"  
Output: false  
Explanation: No permutation of the pattern is present in the given string as a substring.  

Example 3:  
Input: String="bcdxabcdy", Pattern="bcdyabcdx"  
Output: true  
Explanation: Both the string and the pattern are a permutation of each other.  

Example 4:  
Input: String="aaacb", Pattern="abc"  
Output: true  
Explanation: The string contains "acb" which is a permutation of the given pattern.  

'''
# leetcode #567
def find_permutation(string, pattern):
    dic = {}  # records the pattern
    for letter in pattern:
        if letter not in dic:
            dic[letter] = 0
        dic[letter] += 1
    k = len(pattern)
    for i in range(k):
        if string[i] in dic:
            dic[string[i]] -= 1
    for l in range(len(string)-k):
        if string[l+k] in dic:
            dic[string[l+k]] -= 1
        if string[l] in dic:
            dic[string[l]] += 1
        flag = 1
        for d in dic.values():
            if d == 0:
                continue
            else:
                flag = 0
        if flag == 1:
            return True
    return False


if __name__ == '__main__':
    print(find_permutation("aaacb", "abc"))


