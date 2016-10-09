# Import the libraries we need
from bs4 import BeautifulSoup
import csv
import urllib.request

# Read from the page
r = urllib.request.urlopen('https://data.linz.govt.nz/data/?s=r&v=rows').read()

# Set up our BeautifulSoup parser. In this case, I'm using lxml over the regular htmlparser
soup = BeautifulSoup(r, 'lxml')

# Specify which element is closest to the data we want. Closest because the other tags have random garbage names.
entry = soup.find_all('tr', {'data-dojo-type':'K/editing/widgets/ModelObserver'})

# Specify our lists? I'm used to calling them arrays but I think in Python, they're called lists
titles = []
categories = []

# Iterate through each of the titles and get the text out of the a tags
for el in entry:
    titles.append(el.contents[1].a.get_text())

for el in entry:
    categories.append(el.contents[3].a.get_text())

# Create our new CSV in write mode
def write():
    print("Writing to file...")
    with open('names.csv', 'w') as csvfile:
    # Set our writer to use comma as a delimiter and create specific field names
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['Name'])
    # Gotta write the header, y'know
        writer.writeheader()
    # For the length of the titles array (since there are only as many views/downloads etc as datasets)
        for i in range(len(titles)):
        # Spit that data at that index into the CSV
            writer.writerow({ 'Name': titles[i] })
    print("Done")

write()
