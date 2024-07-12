word=input("enter the word")
rev=reversed(word)
if list(word)==list(rev):
    print("its a palindrome")
else:
    print("its not a palindrome")