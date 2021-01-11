from bs4 import BeautifulSoup
import requests
import lxml

base_url = "http://134.122.1.97/"

#Send get http request
page = requests.get(base_url)

#To see the status code of page  (200 is good)
print(page.status_code)

# Verify we had a successful get request
if page.status_code == requests.codes.ok:

    # Get the whole webpage in beautiful soup format
    bs = BeautifulSoup(page.text, 'lxml')

#prints out the whole html page text
# print(page.text)

#Find something you specify in HTML in this case its the list of 'Scrapelus Thisus'
scrapelus = bs.find('ul', id = 'getit').find_all('li')

#NOW TO MANIPULATE THE DATA SCRAPED

#Use Python Indexing to slice thru the list
allsents = scrapelus[0:5]
#print(allsents)


#Will hold our sentences
sentences = {
    'sentence': [],
}


#Get 'sentence' and save it in the data dictionary
one = allsents[0]
if one:
    sentences['sentence'].append(one)
else:
    sentences['sentence'].append('none')
print(one)

#Get 'sentence' and save it in the data dictionary
two = allsents[1]
if two:
    sentences['sentence'].append(two)
else:
    sentences['sentence'].append('none')
print(two)

#Get 'sentence' and save it in the data dictionary
three = allsents[2]
if three:
    sentences['sentence'].append(three)
else:
    sentences['sentence'].append('none')
print(three)

#Get 'sentence' and save it in the data dictionary
four = allsents[3]
if four:
    sentences['sentence'].append(four)
else:
    sentences['sentence'].append('none')
print(four)

#Get 'sentence' and save it in the data dictionary
five = allsents[4]
if five:
    sentences['sentence'].append(five)
else:
    sentences['sentence'].append('none')
print(five)






