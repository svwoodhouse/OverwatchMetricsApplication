from bs4 import BeautifulSoup as bs
import requests
from multiprocessing import Pool
import urllib.request
import time
url = "https://playoverwatch.com/en-us/career/pc/takaharimi-1252"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
page = requests.get(url, headers=header)
soup = bs(page.content, "html.parser")
soup2 = bs(soup.prettify(),"html.parser")
winstonDataFile = open(r"C:\Users\Sydnee\Desktop\OverwatchWebScraper\WinstonData.txt", "w+")
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



#test = soup.findAll("div", {"class":"column lg-8"})
#for x in test:
 #  print(x.find("span").text)


#soup2Test = soup2.findAll("div", {"class":"column xs-12 md-6 xl-4"})
#for x in soup2Test:
   #print(x.find("td")[1].get_text().strip())

#table = soup.findAll("td", {"class":"DataTable-tableColumn"})
#for y in table:
 #  print (y.get_text())

#This code gets the stats from Winston
header = True

characters = {'Ana' : '0x02E000000000013B',
                'Ashe' : '0x02E0000000000200'}
                
winston = "0x02E0000000000009"
for characterName, characterID in characters.items():
   winstonDataFile.write(characterName +" character Data"+ "\n")
   example = soup.findAll("div",{"data-category-id":characterID})
   for e in example:
      data = e.findAll("td",{"class":"DataTable-tableColumn"})
      for d in data:
         if header == True:
            title = d.get_text()
            print(d.get_text()+ " ---------> ", end="")
            winstonDataFile.write(title + " ---------> ")
            header = False
         else:
            stats = d.get_text()
            print(stats +"\n")
            header = True
            winstonDataFile.write(stats + "\n")
   winstonDataFile.write("\n")

winstonDataFile.close()

#bestData = soup.findAll("div", {"class":"column xs-12 md-6 xl-4"})
#for x in bestData:
   #print (x.find("tr").text)
#print(soup.select('td.DataTable-tableColumn'))

#for row in soup.findAll('td.DataTable-tableColumn')[0].tbody.findAll('tr'):
   #title = row.findAll('tr')[0].contents
   #stats = row.findAll('tr')[1].contents
   #print (title + " " + stats)
