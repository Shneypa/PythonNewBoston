import requests
import operator
from bs4 import BeautifulSoup

def crawl(url):
    word_list = []
    source = requests.get(url).text             # treat page as pain text
    soup = BeautifulSoup(source, "html.parser")
    for lines in soup.findAll("li",{"class": "style1"}):
        sentences = lines.string
        words = sentences.lower().split()
        for word in words:
            word_list.append(word)
    cleaned_up_list = cleanup(word_list)


def cleanup(list):
    clean_list = []
    symbols_to_remove = "~!@#$%^&*()_+{}|:\"><?`-=[]\;'./,'"
    for word in list:
        for s in symbols_to_remove:
            word = word.replace(s, "")
        if len(word) > 1:
            clean_list.append(word)
    word_counter(clean_list)

def word_counter(list):
    local_dictionary = {}
    for unique_word in list:
        if unique_word in local_dictionary:
            local_dictionary[unique_word] += 1
        else:
            local_dictionary[unique_word] = 1

    for key, value in sorted(local_dictionary.items(), key = operator.itemgetter(1)):
        print(key, value)

crawl("http://www.staff.science.uu.nl/~hooft101/theorist.html")

