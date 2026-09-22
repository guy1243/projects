#write a program to store birthday dates inside 5 diffrent variables and then print them out in a list
birthday1 = "January 1"
birthday2 = "February 14"
birthday3 = "March 15"
birthday4 = "April 20"
birthday5 = "May 10"
print("Birthday Dates:")
birthdays = [birthday1, birthday2, birthday3, birthday4, birthday5]
for birthday in birthdays:
    print(f"- {birthday}")