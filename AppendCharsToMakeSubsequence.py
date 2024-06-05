def min_chars_to_append(s, t):
    m, n = len(s), len(t)
    i, j = 0, 0
    
    # Find the length of the longest prefix of t that is a subsequence of s
    while i < m and j < n:
        if s[i] == t[j]:
            j += 1
        i += 1
    
    # If j reaches the end of t, it means t is a subsequence of s
    if j == n:
        return 0
    
    # The remaining part of t needs to be appended to s
    return n - j

# Example usage:
s1, t1 = "coaching", "coding"
print(min_chars_to_append(s1, t1))  # Output: 4

s2, t2 = "abcde", "a"
print(min_chars_to_append(s2, t2))  # Output: 0

s3, t3 = "z", "abcde"
print(min_chars_to_append(s3, t3))  # Output: 5

s3, t3 = "cat", "abcde"
print(min_chars_to_append(s3, t3))  # Output: 5
