import os

PROTON_USERNAME = "pspjQPY626AbRbZc"
PROTON_PASSWORD = "7SbTkHModuaXv0RMvJmMxub4IU5z9LqB"

def change_ip():
    os.system(f"protonvpn-cli login {PROTON_USERNAME} {PROTON_PASSWORD}")
    os.system("protonvpn-cli connect --fastest")
    print("✅ IP changed successfully!")
