# By dim1119

import requests
from bs4 import BeautifulSoup
from tweeter import post


def main():
    page = requests.get("http://penteli.meteo.gr/stations/vrilissia/")
    if page.status_code != 200:
        return 1
    soup = BeautifulSoup(page.content, 'html.parser')
    humidity = get_humidity(soup)
    temperature = get_temp(soup)
    print(temperature, humidity)
    post(temperature, humidity)


def get_temp(soup):
    return soup.find_all('div', class_='lright')[0].get_text()


def get_humidity(soup):
    return soup.find_all('div', class_='lright')[1].get_text()


def getnums(input):
    return float(input.split(" ")[0])


if __name__ == "__main__":
    if main() == 1:
        print("Weather Station is not reachable")
