import random

car = ["Tesla Model S",
    "Ford Mustang",
    "Chevrolet Camaro",
    "BMW 3 Series",
    "Honda Civic",
    "Toyota Corolla",
    "Mercedes-Benz C-Class",
    "Audi A4",
    "Jeep Wrangler",
    "Subaru Outback",
    "Volkswagen Golf",
    "Nissan Altima" ]
job = ["Doctor",
    "Teacher",
    "Engineer",
    "Artist",
    "Chef",
    "Scientist",
    "Nurse",
    "Pilot",
    "Software Developer",
    "Lawyer",
    "Photographer",
    "Architect"]
city = ["New York",
    "Paris",
    "Tokyo",
    "Sydney",
    "London",
    "Berlin",
    "San Francisco",
    "Toronto",
    "Singapore",
    "Dubai",
    "Los Angeles",
    "Rome"]
degree = ["Computer Science",
    "Business Administration",
    "Mechanical Engineering",
    "Biology",
    "Psychology",
    "Mathematics",
    "Physics",
    "Electrical Engineering",
    "Art History",
    "Economics",
    "Nursing",
    "Chemical Engineering"]
home = [
    "Mansion",
    "Apartment",
    "Shack",
    "House",
    "Condominium",
    "Townhouse",
    "Cottage",
    "Villa",
    "Bungalow",
    "Loft",
    "Cabin",
    "Farmhouse"]


categories = {"car":car, "city":city, "job":job, "degree":degree, "home":home}

print("Welcome to the game of M.A.S.H\n\nthere are 5 different categories that will determine your life, all by the random role of byte dice")

response = input("Ready to play? y/n: ")


while response.lower() == "y":
    rolled_car = "" 
    rolled_city = ""
    rolled_job = ""
    rolled_degree = ""
    rolled_home = ""
    for category_name, category_list in categories.items():
        
        roll = input("hit Enter to roll, or type 'x' to end the game: ")
        if roll.lower() == "x":
            response = "n"
            break
        else:
            die_roll = random.randint(0,11)
            if category_name == "home":
                print(f"For {category_name}, you got a {category_list[die_roll]}")
                rolled_home = category_list[die_roll]
            elif category_name == "car":
                print(f"For {category_name}, you got a {category_list[die_roll]}")
                rolled_car= category_list[die_roll]
            elif category_name == "city":
                print(f"For {category_name}, you got a {category_list[die_roll]}")
                rolled_city = category_list[die_roll]
            elif category_name == "job":
                print(f"For {category_name}, you got a {category_list[die_roll]}")
                rolled_job = category_list[die_roll]
            elif category_name == "degree":
                print(f"For {category_name}, you got a {category_list[die_roll]}")
                rolled_degree = category_list[die_roll]
            
    print(f"\n\nIn your future, you will drive a {rolled_car}, living in a {rolled_home} in {rolled_city}.\nYou got your degree in {rolled_degree}, however you work as a {rolled_job}.\n\n")
    print("Game finished, hope you're happy with outcome!\n")
    response = input("Play again? y/n: ")
        






