"""
First.py
~~~~~~~~
Extracts name , time and image from gogo-stream and stores in data.json
"""
import json
import requests
import os
from bs4 import BeautifulSoup
import lxml


def start_scraping(FILE='gogo-stream.json'):

    # _ = os.system('clear' if os.name == 'posix' else 'cls')

    URL = 'https://gogo-stream.com/'
    # FILE = 'gogo-stream.json'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'lxml')

    # results=soup.find(id="ResultsContainer")

    # print(results.prettify())

    vid_names = soup.find_all('div', class_='name')
    vid_time = soup.find_all('div', class_='meta')
    temp_image = soup.find_all('div', class_='picture')
    vid_image = []
    for each_image in temp_image:
        # print(each_image.find('img')['src'])
        vid_image.append(each_image.find('img')['src'].strip())

    data = {}
    data['gogo-stream'] = []

    i = 0

    while(i < len(vid_names) and i < len(vid_time) and i < len(vid_image)):
        # print(vid_names[i].text.strip())
        # print(vid_time[i].text.strip())
        # print(vid_image[i].strip())
        # print('-'*5)

        data['gogo-stream'].append({
            'name': vid_names[i].text.strip(),
            'time': vid_time[i].text.strip(),
            'image': vid_image[i].strip()
        })

        i += 1

    with open(FILE, 'w') as outfile:
        try:
            json.dump(data, outfile, indent=4)
        except:
            print("Error occured: ")


if __name__ == '__main__':
    print("***** Started Scraping *****")
    start_scraping()
    print("***** Finished Scraping *****")
