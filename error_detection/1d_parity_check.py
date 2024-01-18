from colorama import Fore

def add_parity(data: str, parity: int) -> str:
    count_ones = data.count('1')

    if (parity == count_ones % 2):
        data += "0"
    else:
        data += "1"

    return data


def check(data: str, parity: int) -> bool:
    count_ones = data[:-1].count('1')

    if (add_parity(data=data[:-1], parity=parity) == data):
        return True
    else:
        return False


def main() -> None:
    tx_num: str = input("\nEnter the data to be transmitted: ").zfill(16)
    parity = int(input("Enter the parity (0 = even & 1 = odd): "))

    rx_num = add_parity(tx_num, parity=parity)
    print("\nParity Bit:", rx_num[-1])
    print("Data after parity:", rx_num)

    received_data = input("\nEnter the received data: ")
    print(f"\nGiven Data: {tx_num}\nTransmitted Data: {rx_num}")

    if (check(received_data.zfill(16), parity=parity) == True):
        print(Fore.GREEN + "The data recieved is Error-free.\n")
    else:
        print(Fore.RED + "The data recieved has an Error.\n")

    return None


if __name__ == '__main__':
    main()
