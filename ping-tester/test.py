import pyshark
import os


INTERFACE_NAME = "Wi-Fi"

capture_size = 0


def capture_packet(time):

    file = "capture.pcapng"
    output = open(file, "w")

    capture = pyshark.LiveCapture(interface=INTERFACE_NAME, output_file=file)
    capture.set_debug()
    capture.sniff(timeout=time)

    output.close()

    return os.path.getsize(file)


time = int(
    input("How long(sec) to capture traffic? [Value should be more than 20 sec]\n")
)

if time < 20:
    print("Timeout must be over 20 seconds.\n")

else:
    print(
        "\nCapture time is: ", time, "sec for each interface.\n\n ....Please wait...."
    )


capture_size = capture_packet(time + 10)

if capture_size >= 1073741824:
    print(
        "|---Total Packet size captured is => ",
        "{0:.2f}".format(capture_size / (1024 * 1024 * 1024)),
        "GB ---|",
    )
elif capture_size >= 1048576:
    print(
        "|---Total Packet size captured is => ",
        "{0:.2f}".format(capture_size / (1024 * 1024)),
        "MB ---|",
    )
elif capture_size >= 1024:
    print(
        "|---Total Packet size captured is => ",
        "{0:.2f}".format(capture_size / 1024),
        "KB ---|",
    )
else:
    print("|---Total Packet size captured is => ", capture_size, "bytes ---|")
