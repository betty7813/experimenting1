str=input("enter a string:")
print(len(str))
print(str.upper())
print(str.lower())
rev=str[::-1]
if str==rev:
    print("palindrome")
else:
    print("not palindrome")
v=0
for i in range(len(str)):
    if str[i] in "AEIOUaeiou":
        ch='_'
        v+=1
print("number of vowels:",v)
