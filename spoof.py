import random

def spoof_number(country_code, phone_number):
    # Generate a random 4-digit suffix and combine it with the provided phone number
    random_suffix = random.randint(1000, 9999)
    return f"{country_code}{phone_number}{random_suffix}"
