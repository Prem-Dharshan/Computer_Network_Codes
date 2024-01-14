
def add_parity(data: str, parity: int) -> str:
    sum = 0
    for i in data:
        if i == "1":
            sum += 1

    if (parity == 1):
        if (sum % 2 == 1):
            data += "0"
        else:
            data += "1"
    else:
        if (sum % 2 == 0):
            data += "0"
        else:
            data += "1"

    return data


def check(data: str, parity: int) -> bool:

    sum = 0
    for i in data[:-1]:
        if i == "1":
            sum += 1

    if (parity == 1):
        if (sum % 2 == 1 and data[-1] == "0"):
            return True
        else:
            return False
    else:
        if (sum % 2 == 0 and data[-1] == "0"):
            return True
        else:
            return False


def main() -> None:

    tx_num: str = input("\nEnter the data to be transmitted: ").zfill(16)
    parity = int(input("Enter the parity (0 = even & 1 = odd): "))

    rx_num = add_parity(tx_num, parity=parity)
    rx_num = input("Enter the recieved data: ")
    print(f"Given Data: {tx_num}\nTransmitted Data: {rx_num}")

    print(f"1D Parity Check: {check(rx_num.zfill(16), parity=parity)}")

    return None


if __name__ == '__main__':
    main()
