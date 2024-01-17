from colorama import Fore


def binary_addition(bin_str1: str, bin_str2: str) -> str:
    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)

    carry = 0
    result = ''

    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if bin_str1[i] == '1' else 0
        r += 1 if bin_str2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    if carry != 0:
        result = binary_addition(result, "1")

    return result


def add_checksum(data: str, k: int) -> str:
    n = len(data)
    k = n // k
    sections = [data[i:i + k] for i in range(0, n, k)]

    checksum = "0"

    for i in range(len(sections)):
        checksum = binary_addition(checksum, sections[i])

    inverted = ''.join('1' if bit == '0' else '0' for bit in checksum)
    checksum = data + inverted

    return checksum


def detect(data: str, k: int) -> bool:
    n = len(data)
    k = n // k
    sections = [data[i:i + k] for i in range(0, n, k)]

    checksum = "0"

    for i in range(len(sections) - 1):
        checksum = binary_addition(checksum, sections[i])

    return checksum != sections[-1]


def main() -> None:
    data = input("Enter the data to be transmitted: ")
    k = int(input("Enter the packet size (k): "))
    tx_data = add_checksum(data, k=k)
    print(f"\nData to be transmitted with checksum: {tx_data}")

    rx_data = input("Enter the received data: ")

    error = detect(rx_data, k=k + 1)

    if not error:
        print(f"\n{Fore.GREEN}The received data is error-free.")
    else:
        print(f"\n{Fore.RED}Error detected in the received data.")


if __name__ == "__main__":
    main()
