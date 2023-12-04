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
page = requests.get(url, headers=header)
bennyPage = requests.get(bennyURL, headers = header)
bennySoup = bs(bennyPage.content,"html.parser")
soup = bs(page.content, "html.parser")
bennySoup = bs(bennyPage.content, "html.parser")

#Text Files containing players Data
characterDataFile = open(r"characterData.txt", "w+")

#Adding the headers to the file
#characterDataFile.write("Hero, Category, Stat, Player\n")

#This function gathers the stats from the different players 
header = True

dataCatagoryID = {}
data=[]

def getDataCatagoryID():
   getMainDiv = soup.findAll("div",{"class":"Profile-heroSummary--view quickPlay-view is-active"})
   for dataCatagories in getMainDiv:
      catagories = dataCatagories.findAll("option")
      for c in catagories:
         catagory = c.get_text()
         catagoryID = c['value']
         dataCatagoryID[catagoryID] = catagory

def getStats(optionID):
   getMainDiv = soup.findAll("div",{"class":"Profile-heroSummary--view quickPlay-view is-active"})
   for dataCatagoryDiv in getMainDiv: 
      getDataCatagoryDiv = soup.findAll("div",{"data-category-id":optionID})
      for characters in getDataCatagoryDiv:
         characterName = characters.findAll("div", {"class": "Profile-progressBar-title"})
         characterStat = characters.findAll("div", {"class": "Profile-progressBar-description"})
         for c, d in zip(characterName, characterStat):
            name = c.get_text()
            stat= d.get_text()
            data.append({"name":name, "title": dataCatagoryID.get(optionID), "stat": stat})

def gatherStats(header, characters, soup, playerName):
   for characterName, characterID in characters.items():
      example = soup.findAll("div",{"data-category-id":characterID})
      for e in example:
         data = e.findAll("td",{"class":"DataTable-tableColumn"})
         for d in data:
            if header == True:
               title = d.get_text()
               #print(d.get_text()+ ", ", end="")
               characterDataFile.write(characterName + "," + title + ",")
               header = False
            else:
               stats = d.get_text()
               #print(stats +"\n")
               header = True
               characterDataFile.write(stats + "," + playerName + "\n")
         #print(characterName + ", " + title + ", " + stats + ", " + playerName + "\n")

getDataCatagoryID()
for i,id in enumerate(dataCatagoryID):
   getStats(id)

# (header,characters,soup,"takaharimi")
# gatherStats(header,characters,bennySoup,"blin1343")
# characterDataFile.close()
# Overwatch_Stats = pd.read_csv("characterData.txt",sep=",", encoding ='unicode_escape', names=["Hero","Category", "Stat", "Player"])
# #print (Overwatch_Stats)
# Medals = Overwatch_Stats[Overwatch_Stats["Category"] == "Medals"]
# Medals["Stat"] = Medals["Stat"].astype(str).astype(int)
# #print(Medals["Stat"])
# Zen = Medals[Medals["Hero"] == "Zenyatta"]
# #Zen["Stat"].astype("int32").dtypes
# Zen.plot(kind = "bar", y="Stat", x="Player")
# #print (list(Overwatch_Stats))
# plt.show()