from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

def main():
    print("Welcome to the Age Calculator!")
    print("Please enter your birthdate.")

    birth_year = int(input("Enter the year (YYYY): "))
    birth_month = int(input("Enter the month (MM): "))
    birth_day = int(input("Enter the day (DD): "))

    age = calculate_age(birth_year, birth_month, birth_day)
    print("You are {} years old.".format(age))

if __name__ == "__main__":
    main()
