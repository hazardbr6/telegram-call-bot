import random

def spoof_number(country_code):
    random_number = random.randint(1000000000, 9999999999)
    return f"{country_code}{random_number}"
