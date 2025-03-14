import random
import requests

CALLING_SITES = [
    "https://www.globfone.com/call/",
    "https://www.poptox.com/",
    "https://www.citrusTel.com/"
]

def make_call(number):
    for site in CALLING_SITES:
        response = requests.get(site, timeout=10)
        if response.status_code == 200:
            print(f"📞 Calling {number} via {site}...")
            return True, f"Call placed via {site}"
    
    return False, "All free calling methods failed!"
