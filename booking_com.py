import requests
from bs4 import BeautifulSoup
import sys  # Import the sys module


class AddressFetcher:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        """Fetch the HTML content of the URL."""
        self.response = requests.get(self.url)
        return self.response.status_code == 200

    def parse_addresses(self):
        """Parse the HTML content to extract addresses."""
        if hasattr(self, 'response'):
            soup = BeautifulSoup(self.response.text, 'html.parser')
            self.address_spans = soup.find_all('span', class_='hp_address_subtitle')
        else:
            print("HTML content has not been fetched. Please run fetch_html() first.")
            self.address_spans = []

    def print_addresses(self):
        """Print the extracted addresses."""
        if hasattr(self, 'address_spans') and self.address_spans:
            print(len(self.address_spans), "addresses found.")
            for address_span in self.address_spans:
                address = address_span.text.strip()
                print("Address:", address)
        else:
            print("No addresses found or parse_addresses() has not been run.")


if __name__ == "__main__":
    if len(sys.argv) > 1:  # Check if a URL was provided
        url = sys.argv[1]  # Get the URL from the command line arguments
        address_fetcher = AddressFetcher(url)

        if address_fetcher.fetch_html():
            address_fetcher.parse_addresses()
            address_fetcher.print_addresses()
        else:
            print("Failed to retrieve the webpage.")
    else:
        print("Please provide a URL as an argument.")
