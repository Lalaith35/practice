#Создать скрипт-скрэппер для получения свежих цитат из топа бездны
#bash.im

# -*- coding: cp1251 -*-

import requests 
import bs4

resp = requests.get("http://bash.im/abysstop")
html = resp.content.decode (resp.encoding)
bs = bs4.BeautifulSoup(html, "html.parser")
quotes = bs.find_all(class_ = "quote")

abysstop = open("abysstop.txt","a",encoding = "utf-8")
abysstop_date = open("abysstop_date.txt","r+",encoding = "utf-8")
abysstop_date_list = abysstop_date.readlines()



for texts in quotes:
#try нужен потому что админы башорга оформл€ют рекламу в класс цитаты
#но такие цитаты нам не нужны, так что если у цитаты нет нужного класса,
#мы еЄ пропускаем
        try:
            t = texts.find(class_ = "abysstop-date")
            t = (t.text+"\n")
            flag = True
            if t in abysstop_date_list:
                flag = False
            if flag:
                abysstop_date.write(t)
                texts = texts.text
                texts = texts.replace("</ br>", "\n")
                texts = texts.replace("<br>", "\n")
                abysstop.write(texts)
        except AttributeError:
            pass
  
        


