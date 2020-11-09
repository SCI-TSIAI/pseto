import requests
from htmldom import htmldom


def create_news_item(node: htmldom.HtmlNodeList):
    date = node.children(".badge").text()
    title = node.children("strong").text()
    content = node.children(".field-name-body").children(".field-items").children(".field-item").text()

    return News(date, title, content)


class News:
    def __init__(self, date, title, content):
        self.date = date
        self.title = title
        self.content = content


site_url = "http://sci.edu.pl"

response = requests.get(site_url)

dom = htmldom.HtmlDom().createDom(response.text)

news_items = [create_news_item(x) for x in dom.find(".news > li")]

news: News
for news in news_items:
    print("Title: {}, Content: {}, Date: {}".format(news.title, news.content, news.date))