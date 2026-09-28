start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

def square_values(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    return squares

def filter_odd_even(squares):
    odd_squares = [x for x in squares if x % 2 == 1]
    even_squares = [x for x in squares if x % 2 == 0]
    return odd_squares, even_squares

squares = square_values(start, end)
odd_squares, even_squares = filter_odd_even(squares)

print("Odd squares:", odd_squares)
print("Even squares:", even_squares)