import os

import ctypes
import requests
import random
import string
import time

from subprocess import call
call('color 2', shell=True)
os.system('color 2')

print("""

███╗░░██╗██╗████████╗██████╗░░█████╗░░   ██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗   ██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║   ██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║   ██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝   ╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░   ╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

                                        ~ Discord Nitro Generator ~ 
                               github.com/rgbkaiser ~ Discord Username : rgbkaiser
""")
time.sleep(0.1)
print("")
time.sleep(0.1)
print("Discord Nitro Generator by Kαιʂҽɾ\n")
time.sleep(0.1)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Nitro Codes.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, be patient if you entered the high number!")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Nitro Codes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" [Valid] >       {nitro} ")
            break
        else:
            print(f" [Invalid] >       {nitro} ")


time.sleep(0.2)

input("\nAll codes have been generated, You will se valid codes in Valid Codes.txt")
input("\nIf the text file is empty, then better luck next time")
