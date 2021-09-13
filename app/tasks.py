from bs4 import BeautifulSoup

import requests


def parse_statisticstimes():
    url = 'https://statisticstimes.com/demographics/countries-by-population.php'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, 'html.parser')

    table = soup.find('table', class_='display').find('tbody')

    pars_data = []
    for item in table:
        # check, the character occurs in the variable and raises an error
        if item != '\n':
            pars_data.append({
                'country': item.find_all('td', class_='name')[0].get_text(strip=True).replace("'", '`'),
                # additionally remove commas
                'population': item.find_all('td', class_='data')[1].get_text(strip=True).replace(',', ''),
                'continent': item.find_all('td', class_='name')[1].get_text(strip=True),
                'source': 'https://statisticstimes.com',
            })
    return pars_data
