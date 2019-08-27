from html.parser import HTMLParser  
from urllib.request import urlopen  
from urllib import parse
from bs4 import BeautifulSoup
import requests
import sys 

######################################
# Web crawler coded in python
#
#
#
######################################

#Creates list to store visited sites
list1 = []


class LinkParser(HTMLParser):

    # This is the orginal function HTMLParser hs
    # We will make some changes to it.


    def handle_starttag(self, tag, attrs):
        # Checks the tag at the beginning of links
        if tag == 'a':
            for (key, value) in attrs:
                if key == 'href':
                    # We are grabbing the new URL from the site. 
                    # We are also adding the base URL to it.            
                    newUrl = parse.urljoin(self.baseUrl, value)

                    list1.append(newUrl)
                    # Adds it to our colection of links:
                    self.links = self.links + [newUrl]
   
   
   
   # This functino will be used to get links
def getLinks(self, url):
        self.links = []
        # Here we will store the base url
        self.baseUrl = url

        # Urlopen function from the standard Python 3 library
        response = urlopen(url)
        print(url)
        # Make sure that we are only looking at HTML
        if response.getheader('Content-Type')=='text/html':
            htmlBytes = response.read()
            
            htmlString = htmlBytes.decode("utf-8")
            self.feed(htmlString)
            return htmlString, self.links
        else:
            return "",[]

# Spider function. Takes a user input for url, word you want to find and the max pages to search

def spider(url, word, maxPages):  
    pagesToVisit = [url]
    numberVisited = 0
    foundWord = False
    # The main loop. Create a LinkParser and get all the links on the page.
    # Also search the page for the word or string
    # In our getLinks function we return the web page
    # (this is useful for searching for the word)
    # and we return a set of links from that web page
    # (this is useful for where to go next)
    while (numberVisited < maxPages) and (pagesToVisit != []) and not foundWord:
        numberVisited = numberVisited +1
        # Start from the beginning of our collection of pages to visit:
        try:
             print(numberVisited, "Visiting:", url)
             parser = LinkParser()
             data, links = parser.getLinks(url)
             list1.pop(0)
             url = list1[0]
            
             if data.find(word)>-1:
                 foundWord = True
                 # Add the pages that we visited to the end of our collection
                 # of pages to visit:
                 pagesToVisit = pagesToVisit + links
                 print(" **Success!**")

        except:
            # Print failed if something wen twrong
             print(" **Failed!**")
        if foundWord:
            # Prints where the word was found
            print("The word", word, "was found at", url)
        else:
            # Else prints word was never found
            print("Word never found")



spider(str(sys.argv[1]),str(sys.argv[2]), int(sys.argv[3]))
