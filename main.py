from bs4 import BeautifulSoup
import requests
import lxml

url = input("The url after refine the search in madlan site:\n")
response = requests.get(url)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")
addresses = soup.find_all(class_="css-1i00gl6")
addresses_list = [address.get_text() for address in addresses]

print(addresses_list)

