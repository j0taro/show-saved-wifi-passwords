import subprocess
from colorama import Fore
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
print("{:<30}      | {:<}".format(f"{Fore.RED} Wi-Fi Name", f"{Fore.RED}Password"))
print(f'{Fore.BLUE}'+f"══════════════════════════════════════════{Fore.RESET}")
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print (Fore.GREEN,"{:<30}{f}| {:<}".format(i,f'{Fore.RED}' +results[0],f=Fore.BLUE))
    except IndexError:
        print (Fore.GREEN,"{:<30}{f}| {:<}]".format(i,f'{Fore.RED}'+ "",f=Fore.BLUE))
input("")
