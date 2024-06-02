from typing import List

def reverse_string(s: List[str]) -> None:
    left,right=0,len(s)-1
    while left < right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    print(s)

s = ["h","e","l","l","o"]
reverse_string(s)