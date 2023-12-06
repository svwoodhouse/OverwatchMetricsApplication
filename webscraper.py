#Library Imports
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
import itertools 

pd.options.mode.chained_assignment = None 
#URL for the Players Data
url = "https://overwatch.blizzard.com/en-us/career/takaharimi-1252/"
bennyURL = "https://overwatch.blizzard.com/en-us/career/blin1343-1104/"

#This grabs the HTML content of the players profile 
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
sydneePage = requests.get(url, headers=header)
bennyPage = requests.get(bennyURL, headers = header)
sydneeSoup = bs(sydneePage.content, "html.parser")
bennySoup = bs(bennyPage.content, "html.parser")

#Text Files containing players Data
characterDataFile = open(r"characterData.txt", "w+")

# Variables used to store proccessed data
# Gets the Category ID used to find the title of each stat
dataCategoryID = {}
# Used to store the scraped data
data=[]

# This function gets the Category IDs that will be used by soup to find the stats for all the different stats
def getDataCategoryID(soup):
   getMainDiv = soup.findAll("div",{"class":"Profile-heroSummary--view quickPlay-view is-active"})
   for dataCategories in getMainDiv:
      categories = dataCategories.findAll("option")
      for c in categories:
         category = c.get_text()
         categoryID = c['value']
         dataCategoryID[categoryID] = category
         
# This function gets the stats based on the different Category IDs passed in
def getStats(optionID, soup):
   getMainDiv = soup.findAll("div",{"class":"Profile-heroSummary--view quickPlay-view is-active"})
   for dataCategoryDiv in getMainDiv: 
      getDataCategoryDiv = dataCategoryDiv.findAll("div",{"data-category-id":optionID})
      for characters in getDataCategoryDiv:
         characterName = characters.findAll("div", {"class": "Profile-progressBar-title"})
         characterStat = characters.findAll("div", {"class": "Profile-progressBar-description"})
         for c, d in zip(characterName, characterStat):
            # Eliminates stats with percentages and any time base data
            if ":" not in d.get_text() and "%" not in d.get_text():
               name = c.get_text()
               stat= d.get_text()
               data.append({"name":name, "title": dataCategoryID.get(optionID), "stat": stat})

# Writes data to the file
def writeDataToFile(data, playerName):
   for i in data:
      characterDataFile.write(i["name"] + "," + i["title"] + "," + i['stat'] + "," + playerName + "\n")

# Gets stats for the player 
getDataCategoryID(sydneeSoup)
for i,id in enumerate(dataCategoryID):
   getStats(id, sydneeSoup)
writeDataToFile(data,"takaharimi")

getDataCategoryID(bennySoup)
for i,id in enumerate(dataCategoryID):
   getStats(id, bennySoup)
writeDataToFile(data,"blin1343")

# Reads in data and displays it as chart
data=pd.read_csv("characterData.txt",sep=",", encoding ='unicode_escape', names=["Hero","Category", "Stat", "Player"])

#bar chart for each character and each category compare the players
data = data[data["Category"].isin(["Eliminations per Life"])]
metric = data["Category"].unique()[0]

df = data.pivot_table(index='Hero',
                  columns='Player', 
                  values='Stat', 
                  fill_value=0, 
                  aggfunc='sum').reset_index()

df.plot(x="Hero", y=[df.columns[1], df.columns[2]], kind="bar") 
plt.xlabel('Hero')  
plt.ylabel(f"{metric}")  
plt.title("Overwatch Stat's Comparison") 
plt.show()
