from subprocess import Popen, PIPE
from re import findall

def ping(host, ping_count, ttl=64):

    for ip in host:
        data = ""
        output = Popen(f"ping {ip} -n {ping_count} -i {ttl}",
                       stdout=PIPE, encoding="utf-8")
        
        # print(output.stdout)

        for line in output.stdout:
            print(line)
            data = data + line
            ping_test = findall("TTL", data)
            # print(data,ping_test)

        if ping_test:
            print(f"{ip} : Successful Ping")
        else:
            print(f"{ip} : Failed Ping")


nodes = ["8.8.8.8", "127.0.0.1", "facebook.com", "psgtech.edu"]

n = int(input("Enter the number of nodes: "))
for i in range(n):
    nodes += input("Enter the IP address: ")

ping_count = int(input("Enter the count of ping: "))

ping(nodes, ping_count=ping_count)