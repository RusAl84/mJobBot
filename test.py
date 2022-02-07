#pip install fuzzywuzzy
#pip install python-Levenshtein
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

sList=["Университет","Проспект Вернадского", "Юго-западная"]
a = process.extractOne("Вернадского", sList)