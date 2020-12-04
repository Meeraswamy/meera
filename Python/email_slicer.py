#This is sample program
import re

adress=input("Enter Your E-mail Adress : ")
pat1=r'^([a-z]+)'
pat2=r'@([a-z]+)'

s1=re.search(pat1,adress)
s2=re.search(pat2,adress)

name=s1.group(1)
domain=s2.group(1)
if domain == "gmail" :print("Hey "+name+", I see your email is registered with Google. That's cool!")
else:print("Hey "+name+", looks like you've got your own custom setup at "+domain+". Impressive!")
