# ==========================================
# TASK 6 - DICTIONARY
# ==========================================


# ------------------------------------------
# Question 1
# Friends' names and length of each name
# ------------------------------------------

friends = [
    "Aditya",
    "Rahul",
    "Suresh",
    "Priya",
    "Anjali"
]

friend_tuples = []

for name in friends:

    friend_tuples.append(
        (name, len(name))
    )


print("Friends and name lengths:")
print(friend_tuples)


# ------------------------------------------
# Question 2
# Expense dictionaries
# ------------------------------------------

your_expenses = {

    "Hotel": 1200,

    "Food": 800,

    "Transportation": 500,

    "Attractions": 300,

    "Miscellaneous": 200
}


partner_expenses = {

    "Hotel": 1000,

    "Food": 900,

    "Transportation": 600,

    "Attractions": 400,

    "Miscellaneous": 150
}


# Calculate total expenses

your_total = sum(
    your_expenses.values()
)

partner_total = sum(
    partner_expenses.values()
)


print("\nYour total expenses:", your_total)

print(
    "Partner's total expenses:",
    partner_total
)


# Determine who spent more

if your_total > partner_total:

    print("You spent more money.")

elif partner_total > your_total:

    print("Your partner spent more money.")

else:

    print("Both spent the same amount.")


# Find category with biggest difference

max_category = ""
max_difference = 0


for category in your_expenses:

    difference = abs(
        your_expenses[category]
        - partner_expenses[category]
    )

    if difference > max_difference:

        max_difference = difference

        max_category = category


print(
    "\nCategory with significant difference:",
    max_category
)

print(
    "Difference:",
    max_difference
)