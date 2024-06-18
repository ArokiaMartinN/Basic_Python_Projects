import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="01234567890"
symbols="!@#$%^&()"
string=lower+upper+numbers+symbols
length=int(input("Type the length of the password:"))
password="".join(random.sample(string,length))
print("Your new password is:",password)