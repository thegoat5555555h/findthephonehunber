import requests
import webbrowser

def search_person_info(name):
    url = f"https://example.com/search?name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        # Extract the relevant information from the response
        phone_number = extract_phone_number(response.text)
        return phone_number
    else:
        return None

def extract_phone_number(html):
    # Use a suitable method (e.g., regular expressions, HTML parsing) to extract the phone number from the HTML
    # Example implementation using regular expressions:
    import re
    phone_number_pattern = r"\d{3}-\d{3}-\d{4}"  # Example pattern for phone number format XXX-XXX-XXXX
    match = re.search(phone_number_pattern, html)
    if match:
        return match.group()
    else:
        return None

# Usage example:
name = input("Enter the person's name: ")
last_name = input("Enter the person's last name: ")
phone_number = search_person_info(name)
if phone_number:
    print(f"Phone number found for {name} {last_name}: {phone_number}")
else:
    print(f"No phone number found for {name} {last_name}")

response = input("Do you want to visit my paypal? (y/n):
