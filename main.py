"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return annual_cost / (credits * SEMESTERS_PER_YEAR)


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return (annual_cost / (credits * SEMESTERS_PER_YEAR)) * (CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER)


def cost_per_credit_load(annual_cost, credits):
    semester_cost = cost_per_semester(annual_cost)
    for load in range(12, 19):
        print(f"{load} credits: ${semester_cost / load:.2f} per credit")



# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    annual_cost = float(input("Enter the total cost for one year: "))
    # Then ask for the credits this semester.
    credits = float(input("Enter the number of credits this semester: "))
    while True:
        # Show your menu here.
        print("\nMenu:")
        print("1. Per semester")
        print("2. Per month")
        print("3. Per class day")
        print("4. Per credit")
        print("5. Per CS 1430 class meeting")
        print("6. Cost per credit at loads from 12 to 18")
        print("Q. Quit")
        choice = input("Choose an option: ")
       
        if choice == "Q":
            break       
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):.2f}") 
        elif choice == "2":
            print(f"Cost per month: ${cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"Cost per CS 1430 class meeting: ${cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            cost_per_credit_load(annual_cost, credits)




# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
