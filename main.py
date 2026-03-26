# Attendance Tracking Mini Project
name = input("Enter Student Name: ")
pattern = input("Enter Attendance Pattern (P/A): ")
total_classes = len(pattern)
present = pattern.count('P')
absent = pattern.count('A')
percentage = (present / total_classes) * 100
print("\n----- Attendance Report-----------")
print("Student Name:", name)
print("Total Classes:", total_classes)
print("Present Days:", present)
print("Absent Days:", absent)
print("Attendance Percentage:", percentage, "%")
if percentage >= 75:
print("Status: Eligible for Exam")
else:
print("Status: Not Eligible for Exam")
