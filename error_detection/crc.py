from sys import stderr
from colorama import Fore

def xor(a, b):

    result = []

    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

def divide(dividend, divisor):

    n = len(divisor)

    tm = dividend[0:n]

    while (n < len(dividend)):
        if tm[0] == '1':
            tm = xor(divisor, tm) + dividend[n]
        else:
            tm = xor('0'*n, tm) + dividend[n]
        n += 1
    if tm[0] == '1':
        tm = xor(divisor, tm)
    else:
        tm = xor('0'*n, tm)

    c = tm
    print("Redundancy bit:", c)
    return c

def endatacode(data, key, remainder):

    a_data = data + remainder
    remainder = divide(a_data, key)
    code = remainder

    return code

def enndatacode(data, key):
    s = len(key)
    a_data = data + "0" * (s-1)
    re = divide(a_data, key)

    return re


def main():

    data = input("Enter the data to be transmitted: ")
    key = input("Enter the key: ")

    ans = enndatacode(data, key)
    print("The data to be transmitted: ", data+ans)

    data1 = input("Enter the recieved data: ")
    ans1 = endatacode(data1, key, ans)

    if (ans1 == len(ans1) * "0"):
        print("The data doesn't have any errors")
    else:
        print(Fore.RED + "The data has errors")


if __name__ == "__main__":
    main()
