import requests
from bs4 import BeautifulSoup
import re
import csv

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the h1 tags and extract the text
    h1_tags = soup.find_all('h1')
    h1_texts = [tag.get_text() for tag in h1_tags]
    
    # Find all the links and extract the href attribute
    links = soup.find_all('a')
    link_hrefs = [link.get('href') for link in links]
    
    # Find all the images and extract the src attribute
    images = soup.find_all('img')
    image_srcs = [image.get('src') for image in images]
    
    # Extract all the email addresses using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, response.text)
    
    # Save the extracted data to a CSV file
    with open('website_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['H1 Tags', 'Links', 'Images', 'Emails'])
        
        for i in range(len(h1_texts)):
            row = [h1_texts[i], link_hrefs[i], image_srcs[i], emails[i]]
            writer.writerow(row)

# Example usage
url = 'https://www.example.com'
scrape_website(url)