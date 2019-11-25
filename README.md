# Overwatch Statistics Comparison Application

This application extracts data of the players of the game Overwatch and compares the statistics between them.\

## Installing
```
git clone git@github.com:svwoodhouse/OverwatchMetricsApplication.git
cd ./OverwatchMetricsApplication
python webscraper.py
```
## Executing Tic Tac Toe Game
Upon exectution of the code, the code grabs the player's information using the request library and using   
```python
url = "https://playoverwatch.com/en-us/career/pc/takaharimi-1252"
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
page = requests.get(url, headers=header)
```
## Built With
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Python library used for pulling data from HTML and XML files.
* [requests](https://pypi.org/project/requests/2.7.0/) - Python library used to send HTTP requests. 
