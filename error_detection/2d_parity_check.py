from typing import List
from colorama import Fore, Style, init

init(autoreset=True)


def add_parity_bit(data: str, parity: int) -> str:
    if parity == 1:
        return "0" if data.count("1") % 2 == 1 else "1"
    else:
        return "0" if data.count("1") % 2 == 0 else "1"


def add_parity(data1: str, data2: str, parity: int) -> str:
    result = ""
    if parity == 1:
        for i in range(len(data1)):
            if data1[i] == data2[i]:
                result += "1"
            else:
                result += "0"
    else:
        for i in range(len(data1)):
            if data1[i] == data2[i]:
                result += "0"
            else:
                result += "1"
    return result


def detect(data: str, parity: int) -> bool:
    n = len(data) // 3
    data1 = data[:n]
    data2 = data[n:n+n]
    par = data[n+n:]

    result = add_parity(data1=data1, data2=data2, parity=parity)

    return result == par


def main() -> None:
    data1: str = input("\nEnter the 1st data to be transmitted: ")
    data2: str = input("\nEnter the 2nd data to be transmitted: ")

    parity = int(input("Enter the parity (0 = even & 1 = odd): "))

    tx_num1: str = data1
    tx_num2: str = data2

    parity_bit1 = add_parity_bit(data=data1, parity=parity)
    parity_bit2 = add_parity_bit(data=data2, parity=parity)

    tx_num1 += parity_bit1
    tx_num2 += parity_bit2

    print(f"Parity bit for Data1: {Fore.BLUE}{parity_bit1}{Style.RESET_ALL}")
    print(f"Parity bit for Data2: {Fore.BLUE}{parity_bit2}{Style.RESET_ALL}")

    print(f"Data to be Transmitted:\n\tTx1: {tx_num1}\n\tTx2: {tx_num2}\n")

    parity_str: str = add_parity(tx_num1, tx_num2, parity=parity)
    print(f"Parity bits for Data1 and Data2: {\
          Fore.BLUE}{parity_str}{Style.RESET_ALL}")

    tx_data = f"{tx_num1}{tx_num2}{parity_str}"
    print(f"Data to be Transmitted: {tx_data}")

    rx_data = input("Enter the received data: ")

    if detect(rx_data, parity) == True:
        print(Fore.GREEN + "No error")
    else:
        print(Fore.RED + "Error")

    return None


if __name__ == '__main__':
    main()
