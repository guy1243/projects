import math

angle = float(input("Enter an angle in degrees: "))

angle_rad = math.radians(angle)
sin_value = math.sin(angle_rad)
cos_value = math.cos(angle_rad)
tan_value = math.tan(angle_rad)

print("The sin of", angle, "degrees is:", sin_value)
print("The cos of", angle, "degrees is:", cos_value)
print("The tan of", angle, "degrees is:", tan_value)