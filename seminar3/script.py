import csv
import string
import re


with open('news.csv', 'r', encoding='utf-8') as file:
    news = csv.DictReader(file)
    news_text = [line['text'] for line in news]

def preprocessing(line):
    line = line.lower()
    print(re.sub(f'[0-9{string.punctuation}==-]+', '', line))
    for sw in stop_words:
        line = line.replace(sw, '')
    return [word for word in line.split() if word not in stop_words]
preprocessing(news_text[0])

with open('stopwords-ru.txt.', 'r'):
    stop_words = {line.strip() for line in file}

print(*news_text[:10], sep='\n')
