from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.a.getText()
    article_texts.append(text)
    link = article_tag.a.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


# print(article_texts)
# print(article_links)
# print(article_upvotes)



























# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.string)
#
# # print(soup.prettify())
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
#      # print(tag.getText())
#      # print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))
#
# name = soup.select_one("#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)




