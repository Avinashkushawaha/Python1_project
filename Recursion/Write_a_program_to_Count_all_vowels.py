def count_vowels(s):
    if len(s) == 0:
        return 0
    else:
        count = 1 if s [0].lower() in 'aeiou' else 0
        return count + count_vowels (s[1:])

check_vowels = input("write in here anything : ")   
print(f" The number of vowels in {check_vowels} is {count_vowels('check_vowels')}")