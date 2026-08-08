import subprocess

profiles = subprocess.check_output(
    "netsh wlan show profiles", shell=True
).decode()

name = [
    line.split(":")[1].strip()
    for line in profiles.split("\n")
    if "All User Profile" in line or "All User Profiles" in line
]

for i, WiFi in enumerate(name, 1):
    print(f"[{i}] {WiFi}")

choice = int(input("\nChoose WiFi Number: "))
WiFi = name[choice - 1]

result = subprocess.check_output(
    f'netsh wlan show profiles "{WiFi}" key=clear',
    shell=True
).decode()

print("\n" + result)