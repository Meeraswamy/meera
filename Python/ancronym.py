#Ancronym Program

ancronym=""
user_in = input("Enter Your Input : ").split(" ")
for i in user_in:
    ancronym+=i[0]

print(ancronym.upper())
