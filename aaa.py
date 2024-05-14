import csv
import requests
from bs4 import BeautifulSoup
import time

# Base URL
base_url = "https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current="

# CSV file path
csv_file_path = 'output.csv'

# Target substring in ID
target_id_substring = "MainContent_MainContent_"

# Additional ID to find
additional_id = "MainContent_litCaption"

# Maximum number of retries
max_retries = 1

# Write header to CSV file
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Get IDs on the first page to create the header
    url = f"{base_url}1"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error on the first attempt: {e}")
        time.sleep(1)
        response = requests.get(url)
        response.raise_for_status()

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    ids = [element['id'] for element in soup.find_all(id=lambda x: x and target_id_substring in x and 'div' not in x)]

    # Write the header
    header = ['Page'] + ids + [additional_id]
    csv_writer.writerow(header)

    # Loop through pages from 1 to 1200
    for page_number in range(1, 1200):
        # Create page URL
        url = f"{base_url}{page_number}"

        # Retry loop
        for retry_count in range(max_retries):
            try:
                # Get HTML content of the page
                response = requests.get(url)
                response.raise_for_status()
                break  # If successful, exit the retry loop
            except requests.exceptions.RequestException as e:
                print(f"Error on attempt {retry_count + 1}: {e}")
                time.sleep(0.1)  # Add a short delay before retrying

        # If all retries failed, skip to the next page
        else:
            print(f"Skipping page {page_number} after {max_retries} failed attempts.")
            continue

        # Parse HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and write ID and content to CSV file
        row_data = [None] * (len(ids) + 2)  # Initialize list to store data for each row
        row_data[0] = page_number  # Set the first element as the page number

        # Get content of each ID
        for idx, id_value in enumerate(ids):
            element = soup.find(id=id_value)
            content = element.get_text(strip=True) if element else ''

            # Assign content to the corresponding column
            row_data[idx + 1] = content

        # Get additional content
        additional_element = soup.find(id=additional_id)
        additional_content = additional_element.get_text(strip=True) if additional_element else ''

        # Assign additional content to the corresponding column
        row_data[-1] = additional_content

        # Write row data to CSV file
        csv_writer.writerow(row_data)

        # Print progress
        print(f"Processed page {page_number}")

print(f"CSV file has been created: {csv_file_path}")
