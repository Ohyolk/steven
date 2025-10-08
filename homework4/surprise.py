# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

def print_star_names(targets):
    for star in targets:
        print(star)

def print_stars_with_type(targets):
    for star in targets:
        print(star, targets[star]["Spectral Type"])

def stars_greater_than_point_one(targets):
    for star in targets:
        if targets[star]["Magnitude"] > 0.1:
            print(star, targets[star]["Magnitude"])

targets["Altair"] = {
    "RA": "19h 50m 47s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}

"""""
def find_closest_to_20(targets):
    closest_star = ""
    smallest_difference = 9999
    for star in targets:
        # i do not know how to do this part
        if difference < smallest_difference:
            smallest_difference = difference
            closest_star = star
    print(closest_star)
"""""
print("My favorite constellation is Orion")
print("All star names:")
print_star_names(targets)

print("Star names with spectral types:")
print_stars_with_type(targets)

print("Stars with magnitude greater than 0.1:")
stars_greater_than_point_one(targets)

print("Star closest to 20° declination:")


# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
