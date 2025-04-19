def reverse_vowels(s: str) -> str:
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer to the next vowel
        while left < right and s_list[left] not in vowels:
            left += 1
        # Move right pointer to the previous vowel
        while left < right and s_list[right] not in vowels:
            right -= 1
        # Swap vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return ''.join(s_list)
print(reverse_vowels("hello"))      # Output: "holle"
print(reverse_vowels("leetcode"))   # Output: "leotcede"
print(reverse_vowels("aA"))         # Output: "Aa"
