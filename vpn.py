import os

PROTON_USERNAME = "pspjQPY626AbRbZc"
PROTON_PASSWORD = "7SbTkHModuaXv0RMvJmMxub4IU5z9LqB"

def change_ip():
    # Use ProtonVPN CLI to change IP (ensure protonvpn-cli is available in your environment)
    os.system(f"protonvpn-cli login {PROTON_USERNAME} {PROTON_PASSWORD}")
    os.system("protonvpn-cli connect --fastest")
    print("✅ IP changed successfully!")
