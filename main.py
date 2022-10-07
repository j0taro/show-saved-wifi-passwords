import subprocess
from colorama import Fore
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    print("{:<30}     | {:<}".format(f"{Fore.RED}Wi-Fi Name", f"{Fore.RED}Password"))
    print(f'{Fore.BLUE}'+f"══════════════════════════════════════════{Fore.RESET}")
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print (f'{Fore.GREEN}'+"{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print (f'{Fore.GREEN}'+"{:<30}| {:<}]".format(i, ""))
input("")
