from colorama import init, Fore

init(autoreset=True)


def xor(op1, op2):
    res = ""
    for i in range(len(op1)):
        if op1[i] == op2[i]:
            res += "0"
        else:
            res += "1"
    return res


def divide(dividend, divisor):
    n = len(divisor)
    n_zeros = (len(divisor) - 1) * "0"
    dividend += n_zeros

    op = dividend[0:n]
    i = n

    while i < len(dividend):
        if op[0] == "0":
            i += 1
            op = op[1:] + (dividend[i] if i < len(dividend) else "")
            continue

        op = xor(op, divisor)[1:]

        i += 1
        if i < len(dividend):
            op += dividend[i]
        else:
            break

    return op


def main():
    dividend = input("Enter the dividend (binary): ")
    divisor = input("Enter the divisor (binary): ")
    n = len(divisor)

    op = divide(dividend=dividend, divisor=divisor)

    appended_dividend = dividend + op
    print("CRC bits:", Fore.GREEN + op)
    print("Appended dividend after CRC:", Fore.GREEN + appended_dividend)

    received_data = input("Enter the received data (binary): ")
    if divide(dividend=received_data, divisor=divisor) == "000":
        print(Fore.GREEN + "Received data is correct!")
    else:
        print(Fore.RED + "Received data is corrupted!")


if __name__ == "__main__":
    main()
