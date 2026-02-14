number_of_days = int(input("Enter the number of days: "))
absences=int(input("Enter the number of absences: "))
attendance_percentage = ((number_of_days - absences) / number_of_days) * 100
print(f"Attendance percentage: {attendance_percentage:.2f}%")
if attendance_percentage >= 75:
    print("You are eligible to take the exam.")
else:    print("You are not eligible to take the exam.")