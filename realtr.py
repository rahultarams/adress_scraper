import re
import sys


class AddressExtractor:
    def __init__(self, url):
        self.url = url

    def extract_address(self):
        # Regular expression to match the address, city, state, and ZIP code part of the URL
        pattern = r'/([^_/]+)-([^_/]+)-([^_/]+)_([^_/]+)_([A-Z]{2})_(\d{5})'

        # Search for the address pattern in the URL
        match = re.search(pattern, self.url)

        if match:
            # Extract address, city, state, and ZIP code
            address = match.group(1).replace('-', ' ')
            address2 = match.group(2).replace('-', ' ')
            address3 = match.group(3).replace('-', ' ')

            city = match.group(4).replace('-', ' ')
            state = match.group(5).replace('-', ' ')
            zip_code = match.group(6)

            # Format the address
            full_address = f"{address}, {address2}, {address3}, {city}, {state} {zip_code}"
            return full_address
        else:
            return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    extractor = AddressExtractor(url)
    address = extractor.extract_address()
    if address:
        print("Address:", address)
    else:
        print("Address not found in the URL.")