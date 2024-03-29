from datetime import datetime, timedelta
from planets import rocky_planets, gas_giants, solar_system
import animate_orbit as draw


def select_date(filename_seed="", year=None, month=None, day=None):
    filename = filename_seed
    print("Enter simulation start date:")
    if(year is None):
        year = int(input("Year>"))
    filename += str(year)
    filename += "-"
    if(month is None):
        month = int(input("Month>"))
    filename += str(month)
    filename += "-"
    if(month is None):
        day = int(input("Day>"))
    filename += str(day)
    filename += ".gif"
    print(filename + " " + year + month + day)
    try:
        date = datetime(year=int(year), month=int(month), day=int(day))
        return date, filename
    except:
        print("Not a valid date. Try again")
        return select_date(filename_seed)


def sim_inner_planets(fileout=False, day=None, year=None, month=None, command=None):
    filename = "rocky_planets-date"

    print("Simulate inner planets")
    date, filename = select_date(filename, year, month, day)

    if not fileout:
        filename = None

    draw.animate_solar_system(rocky_planets, date, timedelta(days=1000),
                              timedelta(days=1), 2, filename, command)


def sim_outer_planets(fileout=False, day=None, year=None, month=None, command=None):
    filename = "gas_giants-date"

    print("Simulate inner planets")
    date, filename = select_date(filename, year, month, day)

    if not fileout:
        filename = None

    draw.animate_solar_system(gas_giants, date, timedelta(days=70000),
                              timedelta(days=70), 35, filename, command)


def get_coordinates():
    print("Enter date:")
    date = select_date()[0]
    print()

    print("Coordinates in the ecliptic plane")
    print("(The plane of the earth's orbit)")
    print("Distances in AU")
    print(date.date())

    for planet in solar_system:
        print_str = planet.name
        print_str += ": ("
        for cord in planet.orbit.get_pos_at_date(date):
            print_str += str((round(cord, 3)))
            print_str += ","

        print_str = print_str.rstrip(print_str[-1])  # hideous way to remove the extra comma
        print_str += ")"
        print(print_str)


def menu():
    while True:
        print("Welcome to the Antikythera")
        print("Your guide to the cosmos")
        print("Enter the option you would like to select:")
        print("1 - Simulate inner planets")
        print("2 - Simulate outer planets")
        print("3 - Find exact coordinates")
        print("x - Exit Program")

        input_str = input(">")

        if input_str == "1":
            sim_inner_planets(True)
        elif input_str == "2":
            sim_outer_planets(True)
        elif input_str == "3":
            get_coordinates()
        elif input_str == "x":
            exit()
        else:
            print("Not a valid command")
            
if __name__ == '__main__':
    menu()