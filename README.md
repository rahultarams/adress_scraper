
# URL Address Extractor Scripts

This repository contains Python scripts that extract addresses from various URLs.

## Requirements Installation

- **Description**: To install the required packages, run the following command:
- **Usage**:
  ```bash
  pip install -r requirements.txt

## Scripts
### 1. `booking_com.py`

- **Description**: This script extracts the address from a booking.com URL HTML parser.
- **Usage**: 
  ```bash
  python booking_com.py <booking.com url>

### 2. `realtr.py`

- **Description**: This script extracts the address from realtor URL using regular expressions.
- **Usage**: 
  ```bash
  python realtr.py <realtor url>

### 3. `redfin.py`

- **Description**: This script extracts the address from redfin URL using regular expressions.
- **Usage**: 
  ```bash
  python redfin.py <redfin url>

### 3. `zillow.py`

- **Description**: This script extracts the address from zillow URL by fetching the contents using a selenium webdriver.
- **Requirements**:
 - Firefox browser
 - geckodriver (Make sure it is installed and added to the system PATH)
- **Usage**: 
  ```bash
  python zillow.py <zillow url>
