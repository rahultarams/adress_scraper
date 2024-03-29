import re
import argparse

class RedfinAddressExtractor:
    def __init__(self, url):
        self.url = url

    def extract_address(self):
        # Regular expression pattern to capture city, state, address, unit/apartment, and home ID from the URL
        pattern = r'https://www.redfin.com/([^/]+)/([^/]+)/(.+?)/([^/]+)/(\d+)'

        match = re.search(pattern, self.url)

        if match:
            state = match.group(1)
            city = match.group(2)
            address = match.group(3).replace('-', ' ')  # Extracting address and removing dashes
            unit_apartment = match.group(4)
            home_id = match.group(5)

            # Combine the parts into the final formatted address
            formatted_address = f"{address} {unit_apartment}, {city}, {state}"

            return formatted_address, home_id
        else:
            return None, None

if __name__ == "__main__":
    # Set up command-line argument parser
    parser = argparse.ArgumentParser(description="Extract address and home ID from a Redfin URL")
    parser.add_argument("url", help="Redfin URL to extract address from")

    # Parse command-line arguments
    args = parser.parse_args()

    # Create an instance of RedfinAddressExtractor with the provided URL
    extractor = RedfinAddressExtractor(args.url)
    address, home_id = extractor.extract_address()

    # Print the extracted address and home ID
    if address and home_id:
        print("Address:", address)
        print("Home ID:", home_id)
    else:
        print("No match found")
