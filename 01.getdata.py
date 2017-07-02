#!/usr/bin/pythonw
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import gzip


def main():
    target_url = 'https://www.zhihu.com/question/55321916'
    data = urllib.request.urlopen(target_url)
    datastr = data.read().decode(encoding='utf-8')
    #print(datastr)


    soup = BeautifulSoup(datastr, 'lxml')
    #print(soup.title)
    #print(soup.title.string)
    maindiv = soup.main.find(name='div', attrs={'itemtype':'http://schema.org/Question'})

    #abstract
    discriptions = maindiv.find_all(tag_has_content)
    question = discriptions[:8]#1-8 question,9-17 answer1...
    for discrip in question:
        print(discrip.get('itemprop') + ' : ' + discrip.get('content'))

    #answers
    answers = maindiv.find_all(class_='List-item')
    print("answer num:" + str(len(answers)))
    for answer in answers:
        for p in answer.find_all('p'):
            print(p.string)
        print("------------------")
    


def tag_has_content(tag):
    return tag.has_attr('content') and tag.get('content') != "" and tag.has_attr('itemprop') and tag.get('itemprop') != ""



if __name__ == '__main__':
    main()
