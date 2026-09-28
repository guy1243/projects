import time

from datetime import date

from dateutil.relativedelta import relativedelta

today = date.today()

valid = False

while not valid:
    try:
        dob = input("please provide your full birthday?: ")

        dob_date = date.fromisoformat(dob)

        age = int(input("Whats your age?: "))

        year = today
      
        delta = relativedelta(year, dob_date).years
        
        if age == delta:
            valid = True

            if age%2 == 0:
                print("Your age is an even number")

            else:
                print("Your age is an odd number")
                
        else:
            print("Please use your real birthday")

    except ValueError:
        print("Please make sure you choose only numbers")

    finally:
        print("\n thanks for trying it out \n")