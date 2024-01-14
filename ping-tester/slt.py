import subprocess
import re


def extract_network_card_info(system_info_output):
    network_card_info_list = []
    network_card_section = re.search(
        r'Ethernet Adapter.*?(?=\n\n|$)', system_info_output, re.DOTALL)

    if network_card_section:
        network_card_info = {}
        lines = network_card_section.group().strip().split('\n')
        for line in lines:
            key_value = re.split(r':\s+', line.strip(), 1)
            if len(key_value) == 2:
                key, value = key_value
                network_card_info[key] = value
        network_card_info_list.append(network_card_info)

    return network_card_info_list


def get_network_card_info():
    try:
        result = subprocess.run(
            'systeminfo', capture_output=True, text=True, check=True)
        system_info_output = result.stdout

        # Extracting information about network cards
        network_card_info_list = extract_network_card_info(system_info_output)

        # Displaying Information about Network Cards
        print("Network Cards Information:")

        if network_card_info_list:
            for index, card_info in enumerate(network_card_info_list, start=1):
                print(f"\nNetwork Card {index}:")
                for key, value in card_info.items():
                    print(f"  {key}: {value}")
        else:
            print("No network card information found.")

    except subprocess.CalledProcessError as e:
        print(f"Error executing SYSTEMINFO: {e}")
        print(f"Error Output: {e.output}")


if __name__ == "__main__":
    get_network_card_info()
