from collections import Counter

def longest_palindrome(s: str) -> int:
    count = Counter(s)
    print("count is :",count)
    length = 0
    odd_found = False
    
    for freq in count.values():
        if freq % 2 == 0:
            length += freq
        else:
            length += freq - 1
            odd_found = True
    
    if odd_found:
        length += 1
        
    return length

# Example usage
input_string = "abccccdd"
print("Length of the longest palindromic sequence is:", longest_palindrome(input_string))
