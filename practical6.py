def calculate_grade(percentage):
    if percentage >= 80:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 40:
        return 'C'
    else:
        return 'D'

try:
    # Get marks for three subjects
    mark1 = float(input("Enter marks for subject 1: "))
    mark2 = float(input("Enter marks for subject 2: "))
    mark3 = float(input("Enter marks for subject 3: "))

    # Calculate total marks
    total_marks = mark1 + mark2 + mark3

    # Calculate percentage
    percentage = (total_marks / 300) * 100

    # Calculate grade
    grade = calculate_grade(percentage)

    # Display the results
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

except ValueError:
    print("Please enter valid numbers for the marks.")

