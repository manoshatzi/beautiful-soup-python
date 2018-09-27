# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.creditkarma.com/credit-cards?ckt=navClickL2'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store the variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of each card and get its value
name_box = soup.find_all('div', attrs={'class':'offer-card-content-right'})

# Extract data from each card
for div in name_box:
    # get the content of each h3>a
    name = div.h3.a.text.strip()
    print(name)
