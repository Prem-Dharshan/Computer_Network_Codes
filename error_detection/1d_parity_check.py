def add_parity(data: str, parity: int) -> str:
    count_ones = data.count('1')

    if (parity == 1 and count_ones % 2 == 1) or (parity == 0 and count_ones % 2 == 0):
        data += "0"
    else:
        data += "1"

    return data


def check(data: str, parity: int) -> bool:
    count_ones = data[:-1].count('1')

    if (parity == 1 and count_ones % 2 == 1 and data[-1] == "0") or \
       (parity == 0 and count_ones % 2 == 0 and data[-1] == "0"):
        return True
    else:
        return False


def main() -> None:
    tx_num: str = input("\nEnter the data to be transmitted: ").zfill(16)
    parity = int(input("Enter the parity (0 = even & 1 = odd): "))

    rx_num = add_parity(tx_num, parity=parity)
    received_data = input("Enter the received data: ")
    print(f"Given Data: {tx_num}\nTransmitted Data: {rx_num}")

    print(f"1D Parity Check: {check(received_data.zfill(16), parity=parity)}")

    return None


if __name__ == '__main__':
    main()
