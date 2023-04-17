# Automating Google Search using Selenium
This code demonstrates how to automate a Google search using Selenium, an open-source tool that allows for browser automation.

## Requirements
Python 3.x
selenium module
Chrome WebDriver

To run this code, you will need to install the selenium module. You can do this by running the following command in your terminal:

pip install selenium

You will also need to download the Chrome WebDriver from the following link: https://sites.google.com/a/chromium.org/chromedriver/downloads

Make sure you choose the version that matches your Chrome browser.

## Usage
Once you have installed the selenium module and downloaded the Chrome WebDriver, you can run the code as follows:

Replace the DOWNLOAD_PATH variable with the path to your downloaded Chrome WebDriver.
Replace the search term in the search.send_keys() method with the term you want to search for on Google.

Run the script in your terminal.

python google_search.py

The script will open a new Chrome window, navigate to Google, search for the term you specified, wait for 5 seconds, and then close the browser.

## References
Selenium Documentation
Chrome WebDriver Downloads