def lengthOfLongestSubstring(s):
        maxLen = 1
        if s == '':
            return 0                      #if there is no string return 0
        for i in range(len(s)):
            substring = s[i]              # Initialising the substring that we will add to.
            for j in range(i+1, len(s)):  # Starting to append characters to substring from i+1
                if s[j] not in substring: # As long as its not repeating. "not in" can be used to check if the character isn't alreadyin the substring
                    substring = substring + s[j]
                    maxLen = max(maxLen, len(substring)) # Updating maxLen if it is greater than the existing maxLen
                else:
                    break
        return maxLen
