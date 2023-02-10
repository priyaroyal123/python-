num=int(input("Enter any number:"))
temp=num
rev=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(temp==rev):
    print("The", temp,"number is palindrome!")
else:
    print(temp ,"Not a palindrome!")
