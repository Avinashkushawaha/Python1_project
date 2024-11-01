def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
user_input = input("Enter here anything: ")    
print(f" {user_input} is a palindrome : {is_palindrome(user_input)}")    
    