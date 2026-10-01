number = int (input("Enter a number: "))

odd_numbers_under = [i for i in range(1, number) if i % 2 != 0]
odd_numbers = [i for i in range(1, number + 1) if i % 2 != 0]

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
updated_fruits = [fruit.capitalize() for fruit in fruits]