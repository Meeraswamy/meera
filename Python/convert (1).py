#this is just sample
amount=float(input("Enter amount u want to convert(only rupees) : "))
print("select to which currency rate i should convert")
print("1 USD \n2 Euro \n3 Yen \n4 Aussie \n ")
rate=input("Enter values shown as above : ")
curr={"USD":(amount//74),"Euro":(amount//88),"Yen":(amount//0.71),"Aussie":(amount//54)}
print(curr[rate])
