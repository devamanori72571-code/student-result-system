student = {
    "name": "Dev",
    "marks": [78, 85, 69]
}

total = sum(student["marks"])
percentage = total / len(student["marks"])

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Name:", student["name"])
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
