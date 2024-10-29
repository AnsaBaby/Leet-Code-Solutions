class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": 
            return 0
        
        current_substring = s[0]
        start_index = 0
        end_index = 1
        max_length = 1
        
        while end_index < len(s):
            if s[end_index] not in current_substring:
                current_substring += s[end_index]
            else:
                while s[start_index] != s[end_index] and start_index < end_index:
                    start_index += 1
                start_index += 1
                current_substring = s[start_index:end_index + 1]
            
            end_index += 1
            if max_length < len(current_substring):
                max_length = len(current_substring)
        
        return max_length

# Time Complexity: O(n)
# Space Complexity: O(k) where k is the size of the character set
