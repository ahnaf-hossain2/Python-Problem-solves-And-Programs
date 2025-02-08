marks = float(input("Enter your marks: "))

if marks >= 0 and marks < 60:
    print("Fail")
elif marks >= 60 and marks <=69:
    print("A-")
elif marks >= 70 and marks <= 79:
    print("A")
elif marks >= 80 and marks <= 100:
    print("A+")
else:
    print("Invalid marks")
