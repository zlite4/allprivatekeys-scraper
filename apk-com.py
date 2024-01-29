
import requests
from bs4 import BeautifulSoup
import csv

# Define the base URL of the website
base_url = 'https://allprivatekeys.com/all-bitcoin-private-keys-list'

# Define the starting page number
starting_page = 400006754326000

# Define the number of pages to scrape
num_pages = 50000

# Define file details
output_file_name = 'positive_balances_output.txt'

# Open the file in write mode
with open(output_file_name, 'w') as output_file:
    # Create a CSV writer if you want to save in CSV format
    # csv_writer = csv.writer(output_file)
    
    # Iterate over the pages
    for page_num in range(starting_page, starting_page - num_pages, -1):
        # Construct the URL for the current page
        url = f'{base_url}?page={page_num}'

        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code != 200:
            print(f'Error: Could not access page {page_num}.')
            continue

        # Parse the HTML content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the table rows containing the private keys and balances
        rows = soup.find_all('tr')

        # Iterate over the rows
        for row in rows:
            # Find the private key and balance columns
            private_key_column = row.find('td', {'class': 'private-key'})
            balance_column = row.find('td', {'class': 'balance'})
            
            # Print for both zero and positive balances to the terminal
            print('Page:', page_num)
            print('Private key:', private_key_column.text)
            print('Balance:', balance_column.text)

            # Check if the balance is positive
            if float(balance_column.text) >= 0:
                # Print to the file only for positive balances
                output_file.write(f'Page: {page_num}\n')
                output_file.write(f'Private key: {private_key_column.text}\n')
                output_file.write(f'Balance: {balance_column.text}\n\n')
