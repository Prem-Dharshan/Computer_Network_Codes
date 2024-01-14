import subprocess
import re


def netstat_analysis():
    # Run the netstat command to get network statistics
    result = subprocess.run(['netstat', '-an'], capture_output=True, text=True)

    # Extract the output from the result
    netstat_output = result.stdout
    print(subprocess.run(['netstat'], capture_output=True, text=True).stdout)
    
    # Analyze the netstat output
    open_ports = re.findall(r'\d+.\d+.\d+.\d+:(\d+)', netstat_output)
    unique_open_ports = set(open_ports)
    total_open_ports = len(unique_open_ports)

    # Display the analysis
    print("Netstat Analysis:")
    print(f"Total Open Ports: {total_open_ports}")
    print("Open Ports:")
    for port in unique_open_ports:
        print(f" - {port}")


if __name__ == "__main__":
    netstat_analysis()
