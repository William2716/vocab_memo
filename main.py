import utils
from datetime import datetime 

utils.creat_folder()
i=1


word=utils.Word(name=input(),date=datetime.now())
word.storage()

