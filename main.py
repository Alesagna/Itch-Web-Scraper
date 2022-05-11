import urllib.request
from bs4 import BeautifulSoup, BeautifulStoneSoup

def itchLookup(genre: str):
    url = (f"https://itch.io/games/tag-{genre}")
    html = urllib.request.urlopen(url)
    htmlParse = BeautifulSoup(html, "html.parser")
    for count in htmlParse.findAll("div", class_="game_title"):
        game_title = count.get_text()
        link_reg = count.find('a', class_="title game_link").get('href')
        print(f"{game_title}, {link_reg}")
if __name__ == "__main__":
    print("Welcome to Ale's Itch Game Fetcher!")
    genre = input("What genre of game do you want?: ")
    itchLookup(genre)