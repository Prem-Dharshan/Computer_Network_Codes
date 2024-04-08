import subprocess

p = subprocess.Popen(["python", "--help"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, errors = p.communicate()

print(output)
