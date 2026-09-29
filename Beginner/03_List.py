# Task 3: List

# Initial Justice League list
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Initial list:", justice_league)


# 1. Calculate number of members
print("Number of members:", len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("After adding members:", justice_league)


# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("After moving Wonder Woman:", justice_league)


# 4. Move Green Lantern between Flash and Aquaman
justice_league.remove("Green Lantern")

aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index, "Green Lantern")

print("After separating Aquaman and Flash:", justice_league)


# 5. Replace the existing list with a new team
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("New Justice League:", justice_league)


# 6. Sort the Justice League alphabetically
justice_league.sort()

print("Alphabetically sorted:", justice_league)


# Hero at index 0 becomes the new leader
print("New leader:", justice_league[0])