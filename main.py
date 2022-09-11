# import csv
import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.theverge.com/"

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)
divs = soup.find_all("div", class_="c-compact-river__entry")

header = ['id', 'URL',
          'headline', 'author', 'date']
with open('ddmmyyy_verge.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
# print(links)
    i = 0
    for it in divs:
        data_list = []
        data_list.append(i)
        url = it.find(
            "a", class_="c-entry-box--compact__image-wrapper", href=True)
        data_list.append(url['href'])
        headline = it.find("h2", class_="c-entry-box--compact__title").string
        data_list.append(headline.strip())
        if it.find("span", class_="c-byline__author-name") == None:
            # print('')
            data_list.append('')
        else:
            authors = ""
            for author in it.find_all("span", class_="c-byline__author-name"):

                authors += author.string.strip()+"\n"
            data_list.append(authors)
            # print()

        if it.find("time", class_="c-byline__item") == None:
            # print('')
            data_list.append('')
        else:
            for date in it.find("time", class_="c-byline__item"):
                # print(date.string)
                data_list.append(date.string.lstrip())
        i = i+1
        writer.writerow(data_list)
