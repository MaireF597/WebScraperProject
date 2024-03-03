from bs4 import BeautifulSoup
import requests


def webScraper(type, search):
    website = 'https://www.wikipedia.org/wiki/'
    #search = 'The_Very_Hungry_Caterpillar'
    result = requests.get(website+search)
    content = result.text #got the content of the website here

    soup = BeautifulSoup(content, 'lxml') #uparse with BeautifulSoup class

    
    #Find the line with Synopsis that's labeled as span in the website content (soup)
    if type == "movie":
        heading = soup.find("span",id="Plot")
    else:
         heading = soup.find("span",id="Synopsis")
    
   
    if heading !=None:
        headingParent = heading.findParent()
        paras = []
        for sib in headingParent.findNextSiblings():
            if sib.name.startswith('h'):
                break
            else:
                paras.append(sib.text.strip())

        for p in paras:
            print(p + '\n')
    else:
        print ("No information found for "+search.replace('_', ' '))



# box2 = soup.find("div",id="mw-content-text")
# print(box2.text)
# paras=""
# for pText in box2.find_all('p'):
#     paras += pText.text
# print (paras)

# print("->")
# print(box1)
# for j in soup.select(''):
#     for i in (j.fetchNextSiblings()):
#             if i.name == 'p':
#                 print(i)



#for sib in soup.find_all('h2'):
#    synopsisText = (sib.find_next_sibling('p')).text 
 #   print(synopsisText)
    


#box = soup.find('h2')
#small = soup.find("span", title=re.compile("Synopsis")).text
#print(small)
#print(box.find_next_siblings('p'))



      
      


