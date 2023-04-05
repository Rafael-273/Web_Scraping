from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://www.zoom.com.br/search?q=rtx%203090&hitsPerPage=48&refinements%5B0%5D%5Bid%5D=price&refinements%5B0%5D%5Branges%5D%5Bmin%5D=1000&refinements%5B0%5D%5Branges%5D%5Bmax%5D=33011.3&sortBy=default&isDealsPage=false&enableRefinementsSuggestions=true'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

prices = []
stores = []

for tag in soup.find_all('p', class_='Text_Text__h_AF6 Text_MobileHeadingS__Zxam2'):
    prices.append(tag.text)

for tag in soup.find_all('h3', class_='Text_Text__h_AF6 Text_MobileLabelXs__ER_cD Text_MobileLabelSAtLarge__YdYbv SearchCard_ProductCard_BestMerchant__f4t5p'):
    stores.append(tag.text)

float_prices = []

for price in prices:
    value = price.split('R$ ')[1]
    value = value.replace('.', '').replace(',', '.')
    float_prices.append(float(value))

min_value = min(float_prices)
min_index = float_prices.index(min_value)

print('---------- Bem Vindo ----------')

print('\n Produto: RTX 3090\n')

print(f'Menor Preço: R${min_value}')
print(stores[min_index], '\n')

print('--------------------------------\n')

while True:
    verify = input('Deseja ver todos os preços/lojas disponíveis? (S/N): ').lower()

    if verify == 's':
        data = {'Loja': stores, 'Preço': float_prices}
        df = pd.DataFrame(data)
        print(df, '\n')
        break
    elif verify == 'n':
        print('OK, sem problemas!')
        break
    else:
        print('Digite uma opção válida')
        continue


