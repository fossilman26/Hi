print("=====================================================")
print("     Welcome to ride builder!                        ")
print("=====================================================")
print()

print("Welcome to ride builder")

print("step 1: pick your vehicle")
print(" 1 - bike")
print(" 2 - car")
print()

choice = int(input("enter 1 or 2: "))
print()

if choice == 1:

    print("step 2: pick your bike type")
    print("  1 - scooty")
    print("  2 - mountain bike")
    print()
    bike_type = int(input("enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("you pick scooty")