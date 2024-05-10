import re
import requests

def extract_images(url):
    response = requests.get(url) 
    html = response.text

    url_pattern = 'https?:\/\/[^\s,]+\.(?:jpg|jpeg|png|gif|bmp)'
    urls = re.findall(url_pattern,html)
    return urls

def main():
    url = "https://www.bol.com"
    urls = extract_images(url)

    for url in urls:
        print(url)

main()