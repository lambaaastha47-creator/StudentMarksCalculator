print("===================================")
print("     STUDENT MARKS CALCULATOR")
print("===================================")

name = input("Enter student name: ")

# Total subjects
subjects = ["English", "Hindi", "Maths", "Science", "Computer"]

marks = []
total = 0

# Input marks for each subject
for subject in subjects:
    while True:
        try:
            mark = int(input("Enter marks in " + subject + " (0-100): "))

            if mark >= 0 and mark <= 100:
                marks.append(mark)
                total = total + mark
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")

# Calculate percentage
percentage = total / len(subjects)

# Calculate result
if any(mark < 33 for mark in marks):
    result = "Fail"
    grade = "F"
elif percentage >= 90:
    result = "Pass"
    grade = "A+"
elif percentage >= 80:
    result = "Pass"
    grade = "A"
elif percentage >= 70:
    result = "Pass"
    grade = "B"
elif percentage >= 60:
    result = "Pass"
    grade = "C"
elif percentage >= 45:
    result = "Pass"
    grade = "D"
else:
    result = "Fail"
    grade = "F"

# Display marksheet
print("\n========== MARKSHEET ==========")
print("Student Name:", name)

for i in range(len(subjects)):
    print(subjects[i] + ":", marks[i])

print("--------------------------------")
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Result:", result)
print("================================")