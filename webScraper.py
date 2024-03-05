from bs4 import BeautifulSoup
import requests


def webScraper(type, search):
    website = 'https://www.wikipedia.org/wiki/'
    result = requests.get(website+search)
    content = result.text #grabs the content of the website here
    
    soup = BeautifulSoup(content, 'lxml') #parses the content with BeautifulSoup class to make it a beautiful soup object
    
    
    #Depending on type argument, finds the line labeled as Plot or Synopsis
    if type == "movie":
        heading = soup.find("span",id="Plot")
        t = "Plot"
    else:
         heading = soup.find("span",id="Synopsis")
         t = "Synopsis"
    
    #Cycles through the website, specifically below the Plot or Synopsis header and returns only the text below the header, halting once a new header is encountered
    if heading !=None:
        #gets parent tag of the heading so that it can search for specific text
        headingParent = heading.findParent()
        #Holds the paragraphs with the text being pulled
        paras = []
        #Cycles through website by finding next node or sibling under the parent
        for sib in headingParent.findNextSiblings():
            if sib.name.startswith('h'):
                break
            else:
                paras.append(sib.text.strip())

        print(t + " for " + search.replace('_', ' ') +":\n")
        for p in paras:
            print(p + '\n')
    else:
        #Prints out if no Synopsis/Plot section is found on the webpage
        print ("No information found for "+search.replace('_', ' '))






      
      


