def gcd_of_lengths(a, b):
    # Function to find GCD of two numbers using Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def gcdOfStrings(str1, str2):
    # Step 1: Check if str1 + str2 == str2 + str1
    if str1 + str2 != str2 + str1:
        return ""  # No common divisor string
    
    # Step 2: Find the GCD of the lengths of str1 and str2
    gcd_length = gcd_of_lengths(len(str1), len(str2))
    
    # Step 3: The largest string that divides both is the substring of length gcd_length
    return str1[:gcd_length]

# Example usage
str1 = "ABCABCABC"
str2 = "ABCABC"
print(gcdOfStrings(str1, str2))  # Output: "ABC"
