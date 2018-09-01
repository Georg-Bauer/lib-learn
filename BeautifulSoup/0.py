# coding: utf-8
from bs4 import BeautifulSoup

if __name__ == "__main__":
    html_doc = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    """
    soup = 0
    link = 0

    soup = BeautifulSoup(html_doc, 'html.parser')
    # 格式化为html
    print soup.prettify()
    # 属性打印
    print soup.title, soup.title.name, soup.title.string, soup.title.parent.name
    print soup.p, soup.p.attrs, soup.p["class"]
    print soup.a, soup.find_all("a")
    print soup.find(id="link3")
    for link in soup.find_all("a"):
        print link["id"], link.get("href")
