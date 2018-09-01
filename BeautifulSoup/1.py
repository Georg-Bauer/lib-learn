# coding: utf-8
from bs4 import BeautifulSoup

if __name__ == "__main__":
    # <class 'bs4.element.Tag'>
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
    # tag
    tag = soup.b
    print type(tag), tag
    # name
    print tag.name
    tag.name = "abcd"
    print tag.name
    # attrs
    print tag.attrs, tag["class"]
    tag["class"] = "hahaha"
    tag["new-attr"] = "hehehe"
    print tag, tag.attrs, tag["class"]
    del tag["class"]
    print tag, tag.attrs
    # 多重attrs
    css_soup1 = BeautifulSoup('<p class="body"></p>', "html.parser")
    css_soup2 = BeautifulSoup('<p class="body strikeout"></p>', "html.parser")
    id_soup1 = BeautifulSoup('<p id="my id"></p>', "html.parser")
    print css_soup1.p["class"], css_soup2.p["class"], id_soup1.p["id"]
    rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>', "html.parser")
    print rel_soup.a['rel']
    rel_soup.a["rel"] = ["index", "contents"]
    print rel_soup

    # <class 'bs4.element.NavigableString'>
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
    tag = soup.b
    print tag.string, type(tag.string)
    unicode_string = unicode(tag.string)
    print unicode_string, type(unicode_string)
    tag.string.replace_with("No longer bold")
    print tag, tag.string

    # <class 'bs4.BeautifulSoup'>
    soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
    print type(soup), soup.name

    # <class 'bs4.element.Comment'>
    soup = BeautifulSoup('<b><!--Hey, buddy. Want to buy a used parser?--></b>', "html.parser")
    comment = soup.b.string
    print type(comment), comment
    print soup.b.prettify()
