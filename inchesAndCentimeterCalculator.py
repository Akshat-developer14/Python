def inchesToCentimeter(inches):
    centimeter = inches * 2.54
    return centimeter


def centimeterToInches(centimeters):
    inchis = centimeters / 2.54
    return inchis


inches = float(input("Enter inches: "))
centimeters = float(input("Enter centimeters: "))
print(f"{inches} inch is equal to {inchesToCentimeter(inches)} centimeter.")
print(f"{centimeters} centimeters is equal to {centimeterToInches(centimeters)} inches.")
