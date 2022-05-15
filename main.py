import urllib.request
from bs4 import BeautifulSoup, BeautifulStoneSoup

def itchLookup(genre: str):
    url = (f"https://itch.io/games/tag-{genre}")
    html = urllib.request.urlopen(url)
    htmlParse = BeautifulSoup(html, "html.parser")
    for i in htmlParse.findAll("div", class_="game_title")[:count]:
        game_title = i.get_text()
        link_reg = i.find('a', class_="title game_link").get('href')
        print("**********")
        print(f"{game_title}, {link_reg}")
if __name__ == "__main__":
    print("Welcome to Ale's Itch Game Fetcher!")
    genre = input("What genre of game do you want?: ")
    while True:
              count = int(input("How many results do you want? [1-36]: "))
              if count < 1 or count > 36:
                  print("Invalid number, try again!")
              else:
                break
    itchLookup(genre)
