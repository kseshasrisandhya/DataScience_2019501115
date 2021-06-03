import requests
from bs4 import BeautifulSoup

def get_links(archive_url):
    r = requests.get(archive_url)
    soup = BeautifulSoup(r.content,"html5lib")
    links = soup.findAll('a')
    links = [link['href'] for link in links if link['href'].endswith('gz')]
    return links

def download_data_files(links):
    for link in links:
        file_name = link.split('/')[-1]  
        print( "Downloading file:%s"%file_name) 
        r = requests.get(link,stream=True)
        with open(file_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

archive_url = "https://datasets.imdbws.com/"
links = get_links(archive_url)
# download_data_files(links)

