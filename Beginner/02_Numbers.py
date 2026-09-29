# ==========================================
# TASK 2 - NUMBERS
# ==========================================

# Question 1
# Using format() function

def format_number(number, character):
    return format(number, character)


result = format_number(145, 'o')

print("Formatted result:", result)


# Question 2
# Area of circular pond
# Formula = pi * r * r

pi = 3.14
radius = 84

area = pi * radius * radius

print("Area of pond:", area, "square meters")


# Bonus Question
# Water = Pond Area * 1.4 liters

water_per_square_meter = 1.4

total_water = area * water_per_square_meter

print("Total water:", int(total_water), "liters")


# Question 3
# Speed = Distance / Time
# Convert minutes into seconds first

distance = 490
time_minutes = 7

time_seconds = time_minutes * 60

speed = distance / time_seconds

print("Speed:", int(speed), "meters per second")