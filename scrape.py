from bs4 import BeautifulSoup
import csv
import urllib

r = urllib.urlopen('https://data.linz.govt.nz/data/').read()
soup = BeautifulSoup(r, 'lxml')
dataset_names = soup.find_all('h4', class_='title')

titles = []

for element in dataset_names:
    titles.append(element.a.get_text())

with open('names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['Name', 'Date', 'Downloads', 'Views'])
    writer.writeheader()
    for a in titles:
        writer.writerow({ 'Name': a.encode('utf-8'), 'Date': 'N/A', 'Downloads': 'N/A', 'Views': 'N/A' })
