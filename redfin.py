import re
import sys

class AddressExtractor:
    def __init__(self, url):
        self.url = url
        self.pattern = r'https://www.redfin.com/([^/]+)/([^/]+)/(.+)/home/(\d+)'

    def extract_and_format_address(self):
        match = re.search(self.pattern, self.url)
        if match:
            state = match.group(1)
            city = match.group(2).replace('-', ' ')
            raw_address = match.group(3)
            home_id = match.group(4)

            street_address = ' '.join(raw_address.split('-')[:-1])
            zip_code = raw_address.split('-')[-1]
            formatted_address = f"{street_address}, {city}, {state} {zip_code}"

            return {"address": formatted_address, "home_id": home_id}
        else:
            return "No match found"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        address_extractor = AddressExtractor(url)
        result = address_extractor.extract_and_format_address()
        print(result)
    else:
        print("Usage: python script_name.py <URL>")
