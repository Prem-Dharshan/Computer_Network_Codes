from colorama import Fore


def xor(a, b):
    result = []
    for i in range(max(len(a), len(b))):
        bit_a = a[i] if i < len(a) else '0'
        bit_b = b[i] if i < len(b) else '0'
        result.append('1' if bit_a != bit_b else '0')
    return ''.join(result)


def divide(dividend, divisor):
    n = len(divisor)
    tm = dividend[0:n]

    while n < len(dividend):
        tm = xor(divisor, tm.ljust(len(divisor), '0')) + dividend[n]
        n += 1

    tm = xor(divisor, tm.ljust(len(divisor), '0'))

    return tm


def add_remainder(data, key, remainder):
    encoded_data = data + remainder
    current_remainder = divide(encoded_data, key)
    return current_remainder


def add_remainder_to_data(data, key):
    s = len(key)
    encoded_data = data + "0" * (s - 1)
    remainder = divide(encoded_data, key)
    return remainder


def calculate_crc(data, key):
    current_remainder = add_remainder_to_data(data, key)
    return current_remainder


def main():
    data = input("Enter the data to be transmitted: ")
    key = input("Enter the key: ")

    current_remainder = calculate_crc(data, key)
    print("The data to be transmitted: ", data + current_remainder)

    received_data = input("Enter the received data: ")
    calculated_remainder = add_remainder(data, key, current_remainder)

    if calculated_remainder == len(calculated_remainder) * "0":
        print("The data doesn't have any errors.")
    else:
        print(f"{Fore.RED}The data has errors.")


if __name__ == "__main__":
    main()
