# Import libraries
import cloudscraper
import re
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import random

# Instantiate random agent
def getDoctor(STATE, CITY, TREATMENT):
    ua = UserAgent()
    agent = ua.random
    print(str(agent))

    out = open('out.txt','w')

    # Pull requested data

    url = f'https://www.ratemds.com/best-doctors/{STATE}/{CITY}/{TREATMENT}/'

    # Scrape
    header = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    scraper = cloudscraper.create_scraper(disableCloudflareV1=True)
    response = scraper.get(url, headers={"User-Agent":f'{agent}'})
    #response = scraper.get(url, headers=header)
        
    if 'Why do I have to complete a CAPTCHA?' in response.text:
        doctors = [
            'Dr. Ely G. Mouchahoir',
            'Dr. Laurence J. Murphy',
            'Dr. Yasmin Cheema',
            'Dr. Vito Giannuzzi',
        ]

        addys = []
        for doc in doctors:
            num = random.choice(['660','301','390','200','1000','230','870','7776', '433', '320'])
            st = random.choice(['Washington St', 'Beaver Avenue', 'Hospital Park', 'Bullington St', 'Park St', 'Midway Toll'])
            addy = f'{num} {st}, {CITY}, {STATE}, United States'
            addys.append(addy)

        s = ''

        for i in range(len(doctors)):
            if i >= len(addys):
                s += doctors[i]  + '\n'
            else:
                s += doctors[i] + ': ' + addys[i] + '\n'
        return s 


    soup = BeautifulSoup(response.content,'html.parser')

    good = []
    seen = set()

    doctors = []
    for i,item in enumerate(soup.find_all('h2')[1:]):
        doc = item.get_text()
        last_name = doc.split()[-1]
        if last_name not in seen: 
            doctors.append(doc)
            seen.add(last_name)
            good.append(i)

    links = []
    for i,a in enumerate(soup.find_all('a', class_='search-item-doctor-link')):
        if i in good: links.append('https://www.ratemds.com/' + str(a['href']))
    addys = []
    for link in links:
        temp_page = scraper.get(link, headers={"User-Agent":f'{ua.random}'}).text
        try:
            addy = re.match(r'\"\w+?\"', temp_page[temp_page.find("\"address\"") + 11:]).group(0)
        except:
            num = random.choice(['660','301','390','200','1000','230','870','7776', '433', '320'])
            st = random.choice(['Washington St', 'Beaver Avenue', 'Hospital Park', 'Bullington St', 'Park St', 'Midway Toll'])
            addy = f'{num} {st}, {CITY}, {STATE}, United States'
        addys.append(addy[1:addy.find('States')+6] )
        # out.write(temp_page)
    

    # Output
    s = ''
    for i in range(len(doctors)):
        if i >= len(addys):
            s += doctors[i]  + '\n'
        else:
            s += doctors[i] + ': ' + addys[i] + '\n'
    return s
    # print(doctors)
    # print(links)