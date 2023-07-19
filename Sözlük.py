import requests
from bs4 import BeautifulSoup
from time import sleep

def kelime_anlamini_ara(kelime):
    url = f"https://www.seslisozluk.net/{kelime}-nedir-ne-demek/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        anlam = soup.find_all("a", lang="tr")
        return anlam
    else:
        return "Kelimenin anlamı bulunamadı."

def main():
    while True:
        kelime = input("Aramak istediğiniz kelimeyi girin (Çıkış için 'q' tuşuna basın): ")
        sleep(1.3)
        if kelime.lower() == "q":
            print("Program sonlandırılıyor...")
            break
        else:
            anlam = kelime_anlamini_ara(kelime)
            print("\n")
            for i in anlam:
                print(i.text)
            print("\n")

if __name__ == "__main__":
    main()