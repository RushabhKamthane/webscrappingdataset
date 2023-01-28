import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests

final = pd.DataFrame()
for j in range(1, 200):
    url = 'https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 6.3;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage = requests.get(url, headers=headers).text
    soup = BeautifulSoup(webpage, 'lxml')
    company = soup.find_all('div', class_='company-content-wrapper')
    name = []
    rating = []
    review_count = []
    ctype = []
    hq = []
    old = []
    employees = []
    for i in company:
        name.append(i.find('h2').text.strip())
        rating.append(i.find('p', class_='rating').text.strip())
        review_count.append(i.find('a', class_='review-count').text.strip())
        ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        hq.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        old.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        try:
            employees.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        except:
            employees.append(np.nan)
    d = {'name': name, 'rating': rating, 'reviews': review_count, 'ctype': ctype, 'hq': hq, 'old': old,
         'employees': employees}
    df = pd.DataFrame(d)
    final = final.append(df, ignore_index=True)


