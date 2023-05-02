import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

day=[0,2,7,30]

class Word:
    def __init__(self,name,date):
        self.name=name
        self.date=date
    def storage(self):
        for i in day:
            with open((self.date+timedelta(days=i)).strftime('%Y_%m_%d')+'/'+self.name+'.txt', 'w', encoding='utf-8') as file:
                looking_up(self.name, file)

def looking_up(name, file):
    url = f'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/{name}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'lxml')

    class_of_words = bs.find_all(class_='pr entry-body__el')

    for class_of_word in class_of_words:
        word_header = class_of_word.find(class_='pos-header dpos-h')

        file.write(f"{word_header.find(class_='pos dpos').text}\n"
                          f"{word_header.find(class_='uk dpron-i').find(class_='region dreg').text} "
                          f"{word_header.find(class_='uk dpron-i').find(class_='pron dpron').text}\n"
                          f"{word_header.find(class_='us dpron-i').find(class_='region dreg').text} "
                          f"{word_header.find(class_='us dpron-i').find(class_='pron dpron').text}\n")

        word_parts = class_of_word.find_all(class_='pr dsense')

        if word_parts:
            for word_part in word_parts:
                file.write(f"{word_part.find(class_='def-block ddef_block').text.strip()}\n")
        else:
            file.write(f"{class_of_word.find(class_='def-block ddef_block').text.strip()}\n")





def creat_folder():
    for i in day:    
        if not os.path.exists((datetime.now()+timedelta(days=i)).strftime('%Y_%m_%d')):
            os.makedirs((datetime.now()+timedelta(days=i)).strftime('%Y_%m_%d'))