#This code compares the stats of two Overwatch Players to see who is better in each category for the different characters in the game
#Character IDs
#All Heroes = 0x02E00000FFFFFFFF
#Ana = 0x02E000000000013B
#Ashe = 0x02E0000000000200
#Baptiste = 0x02E0000000000221
#Bastion = 0x02E0000000000015
#Brigitte = 0x02E0000000000195
#D.Va = 0x02E000000000007A
#Doomfist = 0x02E000000000012F
#Genji = 0x02E0000000000029
#Hanzo = 0x02E0000000000005
#Junkrat = 0x02E0000000000065
#Lucio = 0x02E0000000000079
#McCree = 0x02E0000000000042
#Mei = 0x02E00000000000DD
#Mercy = 0x02E0000000000004
#Moira = 0x02E00000000001A2
#Orisa = 0x02E000000000013E
#Pharah = 0x02E0000000000008
#Reaper = 0x02E0000000000002
#Reinhardt = 0x02E0000000000007
#Roadhog = 0x02E0000000000040
#Sigma = 0x02E000000000023B
#Soldier:76 = 0x02E000000000006E
#Sombra = 0x02E000000000012E
#Symmetra = 0x02E0000000000016
#Torbjorn = 0x02E0000000000006
#Tracer = 0x02E0000000000003
#Widowmaker = 0x02E000000000000A
#Winston = 0x02E0000000000009
#Wrecking Ball = 0x02E00000000001CA
#Zarya = 0x02E0000000000068
#Zenyatta = 0x02E0000000000020

#Library Imports
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None 
#URL for the Players Data
url = "https://playoverwatch.com/en-us/career/pc/takaharimi-1252"
bennyURL = "https://playoverwatch.com/en-us/career/pc/blin1343-1104"

#This grabs the HTML content of the players profile 
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
page = requests.get(url, headers=header)
bennyPage = requests.get(bennyURL, headers = header)
bennySoup = bs(bennyPage.content,"html.parser")
soup = bs(page.content, "html.parser")
bennySoup = bs(bennyPage.content, "html.parser")

#Text Files containing players Data
characterDataFile = open(r"C:\Users\Sydnee\Desktop\OverwatchWebScraper\characterData.txt", "w+")

#Adding the headers to the file
#characterDataFile.write("Hero, Category, Stat, Player\n")

#This function gathers the stats from the different players 
header = True
characters = {'All Heroes' : '0x02E00000FFFFFFFF',
              'Ana' : '0x02E000000000013B',
              'Ashe' : '0x02E0000000000200', 
              'Baptiste' : '0x02E0000000000221',
              'Bastion' : '0x02E0000000000015',
              'Brigitte' : '0x02E0000000000195',
              'D.Va' : '0x02E000000000007A',
              'Doomfist' : '0x02E000000000012F',
              'Genji' : '0x02E0000000000029',
              'Hanzo' : '0x02E0000000000005',
              'Junkrat' : '0x02E0000000000065',
              'Lucio' : '0x02E0000000000079',
              'McCree' : '0x02E0000000000042',
              'Mei' : '0x02E00000000000DD',
              'Mercy' : '0x02E0000000000004',
              'Moira' : '0x02E00000000001A2',
              'Orisa' : '0x02E000000000013E',
              'Pharah' : '0x02E0000000000008',
              'Reaper' : '0x02E0000000000002',
              'Reinhardt' : '0x02E0000000000007',
              'Roadhog' : '0x02E0000000000040',
              'Sigma' : '0x02E000000000023B',
              'Soldier:76' : '0x02E000000000006E',
              'Sombra' : '0x02E000000000012E',
              'Symmetra' : '0x02E0000000000016',
              'Torbjorn' : '0x02E0000000000006',
              'Tracer' : '0x02E0000000000003',
              'Widowmaker' : '0x02E000000000000A',
              'Winston' : '0x02E0000000000009',
              'Wrecking Ball' : '0x02E00000000001CA',
              'Zarya' : '0x02E0000000000068',
              'Zenyatta' : '0x02E0000000000020'}

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

gatherStats(header,characters,soup,"takaharimi")
gatherStats(header,characters,bennySoup,"blin1343")
characterDataFile.close()
Overwatch_Stats = pd.read_csv("C:/Users/Sydnee/Desktop/OverwatchWebScraper/characterData.txt",sep=",", encoding ='unicode_escape', names=["Hero","Category", "Stat", "Player"])
#print (Overwatch_Stats)
Medals = Overwatch_Stats[Overwatch_Stats["Category"] == "Medals"]
Medals["Stat"] = Medals["Stat"].astype(str).astype(int)
#print(Medals["Stat"])
Zen = Medals[Medals["Hero"] == "Zenyatta"]
#Zen["Stat"].astype("int32").dtypes
Zen.plot(kind = "bar", y="Stat", x="Player")
#print (list(Overwatch_Stats))
plt.show()