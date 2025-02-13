mark = int(input("Enter the mark: "))

if(mark <= 100 and mark >= 90):
    grade = "ex"
elif(mark < 90 and mark >= 80):
    grade = "A"
elif(mark < 80 and mark >= 70):
    grade = "B"
elif(mark < 70 and mark >= 60):
    grade = "C"
elif(mark < 60 and mark >= 50):
    grade = "D"
elif(mark < 50 ):
    grade = "F"
print("Your grade is: " + grade)
