from bs4 import BeautifulSoup
import requests

url = 'https://www.kurzy.cz/kurzy-men/nejlepsi-kurzy/EUR-euro/'
try:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        eur_rate = float(soup.span.string)    
    else:
        print('Error parsing')
        
except requests.exceptions.RequestException as e:
    print('Error executing HTTP request', e)


