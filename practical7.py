#using for loop
print("Using for loop:")
print("Feet \t Centimeters")
for f in range(50, 61):  # Multiplying by 10 to handle steps of 0.1
    feet = f / 10
    centimeters = feet * 30.48  # 1 foot = 30.48 cm
    print(f"{feet:.1f} \t {centimeters:.2f}")

#using while loop
print("\nUsing while loop:")
print("Feet \t Centimeters")
f = 5.0
while f <= 6.0:
    centimeters = f * 30.48
    print(f"{f:.1f} \t {centimeters:.2f}")
    f += 0.1
