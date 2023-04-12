import requests
from bs4 import BeautifulSoup

#get the meaning of the word
def get_meaning(word):
    url=f'https://dictionary.cambridge.org/dictionary/english-chinese-simplified/{word}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/55.0.2883.87 Safari/537.36'}
    r = requests.get(url, headers = headers)
    bs = BeautifulSoup(r.text, 'lxml')
    
    class_of_words=bs.find_all(class_='pr entry-body__el')
    

    for class_of_word in class_of_words:
        
        word_header=class_of_word.find(class_='pos-header dpos-h')
        
        
        print(word_header.find(class_='pos dpos').text,'\n' ,word_header.find(class_='uk dpron-i').find(class_='region dreg').text, word_header.find(class_='uk dpron-i').find(class_='pron dpron').text,'\n', word_header.find(class_='us dpron-i').find(class_='region dreg').text, word_header.find(class_='us dpron-i').find(class_='pron dpron').text)

        word_parts=class_of_word.find_all(class_='pr dsense')
        
        if(word_parts):
            for word_part in word_parts:
                print(word_part.find(class_='def-block ddef_block').text)
        else:
            print(class_of_word.find(class_='def-block ddef_block').text)
    
    

get_meaning('word')
print('git can do everything')
#git can do everything