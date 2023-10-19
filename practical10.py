import math

def area_of_rectangle(length, breadth):
    return length * breadth

def area_of_square(side):
    return side * side

def area_of_circle(radius):
    return math.pi * radius * radius

def area_of_triangle(base, height):
    return 0.5 * base * height

while True:
    print("\nMenu:")
    print("1. Area of Rectangle")
    print("2. Area of Square")
    print("3. Area of Circle")
    print("4. Area of Triangle")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        print(f"Area of Rectangle: {area_of_rectangle(length, breadth)}")
    elif choice == '2':
        side = float(input("Enter the side of the square: "))
        print(f"Area of Square: {area_of_square(side)}")
    elif choice == '3':
        radius = float(input("Enter the radius of the circle: "))
        print(f"Area of Circle: {area_of_circle(radius)}")
    elif choice == '4':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(f"Area of Triangle: {area_of_triangle(base, height)}")
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
