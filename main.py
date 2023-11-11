import requests
from bs4 import BeautifulSoup
import lxml

url = "https://rozetka.com.ua/tablets/c130309/"
user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
headers = {"User-agent": user}
session = requests.Session()

for j in range(1, 68):
    print(f"Page{j}")
    url = f"https://rozetka.com.ua/tablets/c130309/page={j}/"
    response = session.get(url, headers=headers)
    # print(response.status_code)

    if response.status_code == 200:
            soup = BeautifulSoup(response.text, "lxml")
            all_products = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
            for i in all_products:
                try:
                    if i.find('div', class_="goods-tile__price--old price--gray ng-star-inserted"):
                        price = i.find('span', class_="goods-tile__price-value")
                        print(price.text)
                        title = i.find('span', class_="goods-tile__title")
                        print(title.text)
                except ValueError:
                    print('Знижки немає')




# a = 10
# b = 0
# try:
#     print(qwerty)
#     c = a / b
# except NameError:
#     print("Такої змінної нема")
#     qwerty = 0
#     print(f'qwerty = {qwerty}')
# except ZeroDivisionError:
#     print("Ділення на 0 заборонено")
#     b = 1
#     c = a / b
