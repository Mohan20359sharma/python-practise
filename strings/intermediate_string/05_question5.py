def find_longest_palindrome(s: str) -> str:
    # Helper function to expand around the center and check for palindrome
    def expand_around_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the palindrome substring

    if len(s) == 0:
        return ""

    longest_palindrome = ""
    
    for i in range(len(s)):
        # Check for odd-length palindromes (single character center)
        odd_palindrome = expand_around_center(i, i)
        if len(odd_palindrome) > len(longest_palindrome):
            longest_palindrome = odd_palindrome
        
        # Check for even-length palindromes (two character center)
        even_palindrome = expand_around_center(i, i + 1)
        if len(even_palindrome) > len(longest_palindrome):
            longest_palindrome = even_palindrome
    
    return longest_palindrome

# Test cases
print(find_longest_palindrome("babad"))  # Output: "bab" or "aba"
print(find_longest_palindrome("cbbd"))   # Output: "bb"
print(find_longest_palindrome("a"))      # Output: "a"
print(find_longest_palindrome("ac"))     # Output: "a" or "c"
