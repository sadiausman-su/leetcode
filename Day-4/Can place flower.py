def can_place_flowers(flowerbed, n):
    i = 0  # index 0 se start kar rahe hain
    length = len(flowerbed)  # total plots kitne hain

    while i < length:
        if flowerbed[i] == 0:  # agar current plot khaali hai
            # left side check karo (agar starting mein ho to OK)
            empty_left = (i == 0) or (flowerbed[i - 1] == 0)

            # right side check karo (agar end mein ho to OK)
            empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)

            # agar dono side khaali hain to flower laga sakte hain
            if empty_left and empty_right:
                flowerbed[i] = 1  # flower laga diya
                n -= 1  # ek flower kam ho gaya

                if n == 0:
                    return True  # agar sare flowers lag gaye to success

                i += 1  # agla plot skip karte hain (adjacent rule)

        i += 1  # har round mein i badha rahe hain

    return n <= 0  # loop ke baad bhi agar n <= 0 hai to return True, warna False
print(can_place_flowers([1, 0, 0, 0, 1], 1))  # Output: True
print(can_place_flowers([1, 0, 0, 0, 1], 2))  # Output: False
