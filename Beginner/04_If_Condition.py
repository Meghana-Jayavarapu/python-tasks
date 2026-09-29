# ==========================================
# TASK 4 - IF CONDITION
# ==========================================


# ------------------------------------------
# Question 1 - BMI Category
# ------------------------------------------

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

bmi = weight / (height ** 2)

print("BMI:", round(bmi, 2))

if bmi >= 30:
    print("Obesity")

elif bmi >= 25:
    print("Overweight")

elif bmi >= 18.5:
    print("Normal")

else:
    print("Underweight")


# ------------------------------------------
# Question 2 - City and Country
# ------------------------------------------

Australia = [
    "Sydney",
    "Melbourne",
    "Brisbane",
    "Perth"
]

UAE = [
    "Dubai",
    "Abu Dhabi",
    "Sharjah",
    "Ajman"
]

India = [
    "Mumbai",
    "Bangalore",
    "Chennai",
    "Delhi"
]

city = input("\nEnter a city name: ")

if city in Australia:
    print(city, "is in Australia")

elif city in UAE:
    print(city, "is in UAE")

elif city in India:
    print(city, "is in India")

else:
    print("City not found")


# ------------------------------------------
# Question 3 - Check Two Cities
# ------------------------------------------

city1 = input("\nEnter the first city: ")
city2 = input("Enter the second city: ")


def find_country(city):

    if city in Australia:
        return "Australia"

    elif city in UAE:
        return "UAE"

    elif city in India:
        return "India"

    else:
        return None


country1 = find_country(city1)
country2 = find_country(city2)


if country1 is not None and country1 == country2:

    print("Both cities are in", country1)

else:

    print("They don't belong to the same country")