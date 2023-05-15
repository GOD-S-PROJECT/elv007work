def reverse_number(num):
    # Convert number to string
    num_str = str(num)

    # Reverse the string
    reversed_str = num_str[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num


# Test the function
number = int(input("Enter a number: "))
reversed_number = reverse_number(number)
print("Reversed number:", reversed_number)