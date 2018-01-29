# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:33:31 2016

@author: smail
"""
import re
import urllib


from bs4 import BeautifulSoup
#### partie qui montre le lien de toutes les régions ###
url = "http://www.mubawab.ma/fr/mp/immobilier-a-vendre"
try:
    
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")
    regions = soup.find('div',{"class":"item-list"}).findAll('a')
    links = re.findall(r'.*?href="(.*?)"',str(regions))
    print links
    print "\nThere are "+str(len(links)) + " regions"
#### FIN de la partie qui montre le lien de toutes les régions ###
    
#### DEBUT partie qui montre les prix ####
    print "\nOpening prices of first page of Casa\n"
    url2 = "http://www.mubawab.ma/fr/crp/grand-casablanca/province-de-m%C3%A9diouna/immobilier-a-vendre"
    page2 = urllib.urlopen(url2)
    soup2 = BeautifulSoup(page2,"html.parser")
    prices = soup2.find_all('div',{"class":"nl-price clickable"})
    prices_str = str(prices)
    
    d = re.findall(r'\b\d+\b',prices_str)
    soup_test = BeautifulSoup(prices_str,"html.parser")
    test = soup_test.find_all('div',{"class":"nl-price clickable"})
    for t in test:
        f = BeautifulSoup(t.text).encode_contents(formatter='html')
#        print f
        s = f.replace("&nbsp","")
        a = s.replace(";","")
        d = re.findall(r'\d+',a)        
        print d
    
except Exception,e:
    print str(e)





