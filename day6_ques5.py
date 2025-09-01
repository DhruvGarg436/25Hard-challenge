# To find out whether the given String is Palindrome or not.
string = input("Enter a string ")
rev = string[::-1]
if string == rev:
    print("Yes,the given string", string, "is palindrome")
else:
    print("No,the given string", string, "is not palindrome")
