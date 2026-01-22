# Student Result Management Project

math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))
urdu = int(input("Enter Urdu marks: "))
computer = int(input("Enter Computer marks: "))


total = math + english + science + urdu + computer
percentage = total / 500 * 100   


if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n-- Student Result --")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)