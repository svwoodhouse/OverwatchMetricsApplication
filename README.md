# Overwatch Statistics Comparison Application

This application extracts data of the players of the game Overwatch and compares the statistics between them.

## Installing
```
git clone git@github.com:svwoodhouse/OverwatchMetricsApplication.git
cd ./OverwatchMetricsApplication
python webscraper.py
```
## Executing Overwatch Metrics Application
Upon exectution of the code, the code grabs the player's information using the request library. 
```python
url = "https://playoverwatch.com/en-us/career/pc/takaharimi-1252"
page = requests.get(url, headers=header)
soup = bs(page.content, "html.parser")
```

 Used Beautiful Soup to filter out the HTMLL content that was given during the request for the player's statistical data.
 Sends the data to a text file and formats it to csv for data processing. 
 ```python
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
```

Used pandas to create a dataframe from the csv file. Extracts the data in the dataframe that shows the total amount of medals each user earned using the character Zenyatta. Displays the data via a bar chart.
```python
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
```

## Built With
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library used for pulling data from HTML and XML files.
* [requests](https://pypi.org/project/requests/2.7.0/) - Python library used to send HTTP requests. 
* [pandas](https://pandas.pydata.org/) - Python open-source library used for data analysis. 
