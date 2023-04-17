# Google Search using Python
This script allows you to perform a Google search using Python and get the URLs of the results.

## Prerequisites
To run this script, you need to have the google package installed. You can install it using pip:


pip install google

## Usage
Import the search function from the googlesearch package:

from googlesearch import search

## Define the search query:

query = "Medium.com"

## Iterate over the results and print the URLs:

for url in search(query):
    print(url)
    
## Note
Please note that this script uses Google's search API, and there are some limitations on the usage. Make sure to read Google's terms of service before using this script in your project.