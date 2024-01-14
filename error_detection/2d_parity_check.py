from typing import List
from colorama import Fore

def add_parity_bit(data: str, parity: int) -> str:

    sum: int = 0

    for i in data:
        if i == "1":
            sum += 1

    if (parity == 1):
        if (sum % 2 == 1):
            return "0"
        else:
            return "1"
    else:
        if (sum % 2 == 0):
            return "0"
        else:
            return "1"


def add_parity(data1: str, data2: str) -> str:

    result = ""

    for i in range(-1, len(data1)):
        if (data1[i] == data2[i]):
            result = "1" + result
        else:
            result = "0" + result

    parity_val = "0" if result.count("1") % 2 == 0 else "1"

    return parity_val


def detect(data1: str, data2: str, bit) -> bool:

    result = ""

    for i in range(-1, len(data1)):
        if (data1[i] == data2[i]):
            result = "1" + result
        else:
            result = "0" + result

    parity_val = "0" if result.count("1") % 2 == 0 else "1"

    return True if parity_val == bit else False


def main() -> None:

    data1: str = input("\nEnter the 1st data to be transmitted: ").zfill(8)
    data2: str = input("\nEnter the 2nd data to be transmitted: ").zfill(8)
    # print(data1, data2)

    parity = int(input("Enter the parity (0 = even & 1 = odd): "))

    tx_num1: str = data1
    tx_num2: str = data2

    tx_num1 = f"{tx_num1}{add_parity_bit(data=data1, parity=parity)}"
    tx_num2 = f"{tx_num2}{add_parity_bit(data=data2, parity=parity)}"
    print(f"Data to be Transmitted: {tx_num1}\n{tx_num2}")

    parity_bit: str = add_parity(tx_num1[:-1], tx_num2[:-1])
    tx_data = f"{tx_num1[:-1]}{tx_num2[:-1]}{parity_bit}"
    print(f"Data to be Transmitted: {tx_data}")

    rx_num1 = input("Enter the recieved data1: ")
    rx_num2 = input("Enter the recieved data2: ")

    if detect(rx_num1, rx_num2, parity_bit) == True:
        print("No error")
    else:
        print(Fore.RED + "Error")

    return None


if __name__ == '__main__':
    main()
