def string_score(s):
    total_score = 0
    for i in range(len(s) - 1):
        total_score += abs(ord(s[i]) - ord(s[i + 1]))
    return total_score

# Example usage:
s = "hello"
print(string_score(s))  # Output: 13
