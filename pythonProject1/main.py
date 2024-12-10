number=int(input("enter the number:"))
temp=number
reverse=0
while number>0:
    digit=number%10
    reverse=reverse*10+digit
    number=number//10
if temp==reverse:
    print("the number is a palindrome!")
else:
    print("not a plaindrome!")
input_string=input("enter a string:")
if input_string=input_string[::-1]:
    print("the string is a palindrome")
else:
print("not  a palindrome")