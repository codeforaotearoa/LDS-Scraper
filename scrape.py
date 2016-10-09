# Import the libraries we need
from bs4 import BeautifulSoup
import csv
import urllib

# Read from the page
r = urllib.urlopen('https://data.linz.govt.nz/data').read()

# Set up our BeautifulSoup parser. In this case, I'm using lxml over the regular htmlparser
soup = BeautifulSoup(r, 'lxml')

# Specify which element is closest to the data we want. Closest because the other tags have random garbage names.
dataset_titles = soup.find_all('h4', class_='title')
download_counter = soup.find_all('i', class_="fa fa-download")
view_counter = soup.find_all('i', class_="fa fa-signal")

# Specify our lists? I'm used to calling them arrays but I think in Python, they're called lists
titles = []
downloads = []
views = []

# Iterate through each of the titles and get the text out of the a tags
for element in dataset_titles:
    titles.append(element.a.get_text())

# Iterate through each of the download counts by connecting to the i tag then getting the next sibling
for element in download_counter:
    downloads.append(element.next_sibling.get_text())

# Ditto for the views
for element in view_counter:
    views.append(element.next_sibling.get_text())

# Create our new CSV in write mode
def write():
    print "Writing to file..."
    with open('names.csv', 'w') as csvfile:
    # Set our writer to use comma as a delimiter and create specific field names
        writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=['Name', 'Date', 'Downloads', 'Views'])
    # Gotta write the header, y'know
        writer.writeheader()
    # For the length of the titles array (since there are only as many views/downloads etc as datasets)
        for i in xrange(len(titles)):
        # Spit that data at that index into the CSV
            writer.writerow({ 'Name': titles[i], 'Date': 'N/A', 'Downloads': downloads[i], 'Views': views[i] })
    print "Done"

write()
