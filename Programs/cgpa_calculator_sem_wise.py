# Given data
current_cgpa = float(input("Enter your current CGPA: "))
completed_credits = int(input("Enter the completed credits: "))
new_sgpa = float(input("Enter the new SGPA: "))
new_credits = int(input("Enter the new credits: "))

# Calculate new CGPA
new_cgpa = ((current_cgpa * completed_credits) + (new_sgpa * new_credits)) / (completed_credits + new_credits)
print(f"Your new CGPA is: {new_cgpa:.2f}")
