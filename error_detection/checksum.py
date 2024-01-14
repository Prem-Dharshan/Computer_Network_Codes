from colorama import Fore

def binary_addition(bin_str1, bin_str2):

    max_len = max(len(bin_str1), len(bin_str2))
    bin_str1 = bin_str1.zfill(max_len)
    bin_str2 = bin_str2.zfill(max_len)
    # print(f"Operands: {bin_str1}, {bin_str2}")

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

def add_checksum(data, k):

    n = len(data)
    k = n//k
    sections = [data[i:i+k] for i in range(0,n,k)]

    checksum = "0"

    for i in range(len(sections)):
        checksum = binary_addition(checksum, sections[i])
    
    inverted = ''.join('1' if bit == '0' else '0' for bit in checksum)
    checksum = data + inverted

    return checksum

def detect(data, k):

    n = len(data)
    k = n//k
    sections = [data[i:i+k] for i in range(0, n, k)]
    # print(f"Det sections: {sections}")

    checksum = "0"

    for i in range(len(sections)):
        checksum = binary_addition(checksum, sections[i])
        # print(f"Checksum: {checksum}")
    
    return all(bit == '1' for bit in checksum)


def main():

    data = input("Data: ")
    k = int(input("Enter the k: "))
    tx_data = add_checksum(data, k=k)
    print(f"Data to be transmitted: {tx_data}")

    rx_data = input("Enter the recieved data: ")

    error = detect(rx_data, k=k+1)

    if error == False:
        print(f"{Fore.RED}An error has been detected in the recieved data.")
    else:
        print(f"The recieved data doesn't have any errors.")

    return None

if __name__ == "__main__":
    main()