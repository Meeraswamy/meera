while True:
    name=input("Enter your name :")
    if name.isalpha:
        break
    else:continue
adress=input("Enter your adress (city,country) :")
dob=input("Enter your Date Of Birth (dd/mm/yyyy) :")
goal=input("Enter your goal :")

print("  ")
print("- Name : "+name)
print("- Date Of Birth : "+dob.replace("/","-"))
print("- Adress : "+adress)
print("- Personnel Goal : "+goal)
