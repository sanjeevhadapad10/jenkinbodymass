# attendance_tracker.py

# Input from user
total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

# Validation
if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input! Please enter correct values.")
else:
    # Calculate attendance percentage
    attendance_percentage = (attended_classes / total_classes) * 100
    
    # Display result
    print("Attendance Percentage:", round(attendance_percentage, 2), "%")
