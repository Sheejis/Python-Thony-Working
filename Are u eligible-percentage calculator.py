print("Are you eligible for admission:")
No1=int(input("obtain marks:"))
No2=int(input("total marks:"))
percent=(No1/No2*100)
print("your percentage is:", percent, "%")

if percent>=60:
    print("you are eligible")
else:
    print("you are not eligible")
    