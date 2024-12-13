from itertools import permutations


def hex_to_dec(hex_str):
    """Convert a hexadecimal string to a decimal integer."""
    return int(hex_str, 16)


def digital_root(num):
    """Calculate the digital root of a number."""
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


def calculate_hex_statistics(hex_chars):
    """Calculate the sum and digital root of the max, min, and median values."""
    # Generate all permutations of the input characters
    permutations_list = ["".join(p) for p in permutations(hex_chars)]

    # Convert permutations to decimal values
    decimal_values = sorted(hex_to_dec(p) for p in permutations_list)

    # Find max, min, and median values
    max_value = decimal_values[-1]
    min_value = decimal_values[0]

    n = len(decimal_values)
    if n % 2 == 1:
        median_value = decimal_values[n // 2]
    else:
        median_value = (decimal_values[n // 2 - 1] + decimal_values[n // 2]) // 2

    # Calculate the sum of max, min, and median
    total_sum = max_value + min_value + median_value

    # Calculate the digital root of the sum
    result = digital_root(total_sum)

    return result


# Input and output handling
if __name__ == "__main__":
    # Input: space-separated characters
    hex_chars = input().split()

    # Compute the result
    result = calculate_hex_statistics(hex_chars)

    # Output the result
    print(result)
