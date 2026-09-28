def decimal_to_binary(decimal):
    if decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    binary = ""
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    
    return binary